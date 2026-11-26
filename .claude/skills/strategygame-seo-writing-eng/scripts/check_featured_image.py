"""Check a StrategyGame post body before publishing (Python standard library)."""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

SITE = 'https://strategygame.org/'

def asset_key(url):
    """Identify a WordPress asset across thumbnail sizes, format conversions and CDN aliases."""
    if not url or url.startswith('data:'):
        return None
    parsed = urlsplit(urljoin(SITE, url))
    path = unquote(parsed.path)
    marker = '/wp-content/uploads/'
    if marker in path:
        directory, _, filename = path.split(marker, 1)[1].rpartition('/')
        filename = re.sub(r'(?:\.(?:jpe?g|png|webp|avif|gif))+$', '', filename, flags=re.I)
        filename = re.sub(r'(?:-\d{2,5}x\d{2,5}|-scaled|-rotated)+$', '', filename)
        return ('uploads', directory, filename)
    return (parsed.netloc.lower(), path)

class BodyImages(HTMLParser):
    def __init__(self, url, attachment_id):
        super().__init__()
        self.cover = asset_key(url)
        self.attachment_id = str(attachment_id) if attachment_id else None
        self.errors = set()

    def match_url(self, url):
        if self.cover and asset_key(url) == self.cover:
            self.errors.add('featured asset appears in article imagery')

    def match_id(self, value):
        if self.attachment_id and str(value) == self.attachment_id:
            self.errors.add('featured attachment ID appears in article imagery')

    def handle_comment(self, text):
        m = re.match(r'\s*wp:(?:core/)?([\w-]+)\b(.*)', text, re.S)
        if not m:
            return
        block, rest = m.groups()
        if block == 'post-featured-image':
            self.errors.add('Gutenberg featured-image block in article body')
        elif block in ('image', 'cover', 'gallery') and rest.strip().startswith('{'):
            attrs, _ = json.JSONDecoder().raw_decode(rest.lstrip())
            self.match_id(attrs.get('id'))
            for value in attrs.get('ids', []):
                self.match_id(value)
            self.match_url(attrs.get('url'))

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = (a.get('class') or '').split()
        if 'wp-block-post-featured-image' in classes:
            self.errors.add('rendered featured-image block in article body')
        if tag not in ('img', 'source'):
            return
        if self.attachment_id and 'wp-image-'+self.attachment_id in classes:
            self.match_id(self.attachment_id)
        for key in ('data-id','data-attachment-id'):
            self.match_id(a.get(key))
        for key in ('src','data-src','data-lazy-src','data-original','data-full-url'):
            self.match_url(a.get(key))
        for key in ('srcset','data-srcset','data-lazy-srcset'):
            for candidate in (a.get(key) or '').split(','):
                fields = candidate.split()
                if fields:
                    self.match_url(fields[0])

def check_body(content, cover_url, attachment_id=None):
    check = BodyImages(cover_url, attachment_id)
    check.feed(content)
    check.close()
    return sorted(check.errors)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('body', type=Path, help='raw Gutenberg body or rendered entry content only')
    parser.add_argument('--cover', required=True, help='featured media or actual Open Graph image URL')
    parser.add_argument('--id', type=int, help='WordPress featured media attachment ID')
    args = parser.parse_args()
    errors = check_body(args.body.read_text(), args.cover, args.id)
    for error in errors:
        print('FAIL', error)
    if errors:
        raise SystemExit(1)
    print('PASS featured image is distinct from the article body')
