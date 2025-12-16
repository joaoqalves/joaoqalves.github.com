#!/usr/bin/env python3
"""
Import posts from an Atom feed into Hugo blog.
This script is idempotent - it won't create duplicate posts.
"""

import xml.etree.ElementTree as ET
import html
import re
import os
from datetime import datetime
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
from urllib.request import urlopen, Request

# Namespace for Atom feeds
ATOM_NS = {'atom': 'http://www.w3.org/2005/Atom'}


class HTMLToMarkdownConverter(HTMLParser):
    """Simple HTML to Markdown converter for basic formatting."""
    
    def __init__(self):
        super().__init__()
        self.markdown = []
        self.current_tag = None
        self.list_depth = 0
        self.in_code = False
        
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        
        if tag == 'h1':
            self.markdown.append('\n# ')
        elif tag == 'h2':
            self.markdown.append('\n## ')
        elif tag == 'h3':
            self.markdown.append('\n### ')
        elif tag == 'h4':
            self.markdown.append('\n#### ')
        elif tag == 'p':
            self.markdown.append('\n\n')
        elif tag == 'br':
            self.markdown.append('\n')
        elif tag == 'strong' or tag == 'b':
            self.markdown.append('**')
        elif tag == 'em' or tag == 'i':
            self.markdown.append('*')
        elif tag == 'code':
            self.markdown.append('`')
            self.in_code = True
        elif tag == 'pre':
            self.markdown.append('\n```\n')
        elif tag == 'ul':
            self.list_depth += 1
        elif tag == 'ol':
            self.list_depth += 1
        elif tag == 'li':
            indent = '  ' * (self.list_depth - 1)
            if self.current_tag == 'ul':
                self.markdown.append(f'\n{indent}- ')
            else:
                self.markdown.append(f'\n{indent}1. ')
        elif tag == 'blockquote':
            self.markdown.append('\n> ')
        elif tag == 'a':
            href = dict(attrs).get('href', '')
            self.markdown.append('[')
            self.link_href = href
        elif tag == 'img':
            src = dict(attrs).get('src', '')
            alt = dict(attrs).get('alt', '')
            self.markdown.append(f'![{alt}]({src})')
            
    def handle_endtag(self, tag):
        if tag == 'strong' or tag == 'b':
            self.markdown.append('**')
        elif tag == 'em' or tag == 'i':
            self.markdown.append('*')
        elif tag == 'code':
            self.markdown.append('`')
            self.in_code = False
        elif tag == 'pre':
            self.markdown.append('\n```\n')
        elif tag == 'ul' or tag == 'ol':
            self.list_depth = max(0, self.list_depth - 1)
        elif tag == 'p':
            pass  # Already handled
        elif tag == 'a':
            if hasattr(self, 'link_href'):
                self.markdown.append(f']({self.link_href})')
                delattr(self, 'link_href')
        elif tag in ['h1', 'h2', 'h3', 'h4']:
            self.markdown.append('\n')
        
        self.current_tag = None
        
    def handle_data(self, data):
        if not self.in_code:
            # Clean up whitespace but preserve structure
            data = data.strip()
            if data:
                self.markdown.append(data)
        else:
            self.markdown.append(data)
            
    def get_markdown(self):
        result = ''.join(self.markdown)
        # Clean up multiple newlines
        result = re.sub(r'\n{3,}', '\n\n', result)
        return result.strip()


def html_to_markdown(html_content):
    """Convert HTML content to Markdown."""
    # First, unescape HTML entities
    html_content = html.unescape(html_content)
    
    # Remove the outer div.trix-content wrapper if present
    html_content = re.sub(r'^<div class="trix-content">\s*', '', html_content)
    html_content = re.sub(r'\s*</div>\s*$', '', html_content)
    
    # Try markdownify first (best option)
    try:
        from markdownify import markdownify as md
        result = md(html_content, heading_style="ATX", bullets="-")
        return result.strip()
    except ImportError:
        pass
    
    # Try html2text as fallback
    try:
        import html2text
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.body_width = 0  # Don't wrap lines
        markdown = h.handle(html_content)
        return markdown.strip()
    except ImportError:
        # Fallback to simple converter
        converter = HTMLToMarkdownConverter()
        converter.feed(html_content)
        return converter.get_markdown()


def slugify(text):
    """Convert text to a URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def extract_entry_id(entry_id):
    """Extract a unique identifier from entry ID."""
    # Entry IDs look like: tag:world.hey.com,2005:World::Post/46064
    match = re.search(r'/(\d+)$', entry_id)
    if match:
        return match.group(1)
    return entry_id.split('/')[-1] if '/' in entry_id else entry_id


def fetch_atom_feed(url):
    """Download Atom feed from URL and return root element and next page URL."""
    print(f"Downloading: {url}")
    # Add User-Agent header to avoid being blocked
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; AtomFeedImporter/1.0)'})
    with urlopen(req) as response:
        content = response.read()
        root = ET.fromstring(content)
    
    # Find next page link
    atom_ns = 'http://www.w3.org/2005/Atom'
    next_url = None
    for link in root.findall(f'{{{atom_ns}}}link'):
        if link.get('rel') == 'next':
            next_url = link.get('href')
            break
    
    return root, next_url


def parse_atom_feed(root):
    """Parse the Atom feed root element and return list of entries."""
    # Atom namespace
    atom_ns = 'http://www.w3.org/2005/Atom'
    
    entries = []
    # Find all entries using the namespace
    for entry in root.findall(f'.//{{{atom_ns}}}entry'):
        entry_id = entry.find(f'{{{atom_ns}}}id')
        published = entry.find(f'{{{atom_ns}}}published')
        updated = entry.find(f'{{{atom_ns}}}updated')
        title = entry.find(f'{{{atom_ns}}}title')
        content = entry.find(f'{{{atom_ns}}}content')
        
        # Find link with rel="alternate"
        link = None
        for link_elem in entry.findall(f'{{{atom_ns}}}link'):
            if link_elem.get('rel') == 'alternate':
                link = link_elem
                break
        
        if entry_id is None or published is None or title is None or content is None:
            continue
            
        entries.append({
            'id': entry_id.text if entry_id is not None else '',
            'published': published.text if published is not None else '',
            'updated': updated.text if updated is not None else '',
            'title': title.text if title is not None else '',
            'content': content.text if content is not None else '',
            'link': link.get('href') if link is not None else '',
        })
    
    return entries


def find_existing_post_by_id(posts_dir, entry_id):
    """Check if a post with this entry ID already exists."""
    entry_id_short = extract_entry_id(entry_id)
    
    for file_path in Path(posts_dir).glob('*.markdown'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Check if entry_id is in frontmatter
                if f'entry_id: "{entry_id}"' in content or f'entry_id: {entry_id}' in content:
                    return file_path
                # Also check for short ID
                if f'entry_id: "{entry_id_short}"' in content or f'entry_id: {entry_id_short}' in content:
                    return file_path
        except Exception:
            continue
    return None


def create_post_file(posts_dir, entry):
    """Create a Hugo post file from an Atom entry."""
    # Parse published date
    try:
        pub_date = datetime.fromisoformat(entry['published'].replace('Z', '+00:00'))
    except Exception:
        pub_date = datetime.now()
    
    # Generate filename
    title_slug = slugify(entry['title'])
    filename = f"{pub_date.strftime('%Y-%m-%d')}-{title_slug}.markdown"
    file_path = Path(posts_dir) / filename
    
    # Check if post already exists (idempotency)
    existing = find_existing_post_by_id(posts_dir, entry['id'])
    if existing:
        print(f"✓ Post already exists: {existing.name} (entry_id: {extract_entry_id(entry['id'])})")
        return False
    
    # Convert HTML to Markdown
    markdown_content = html_to_markdown(entry['content'])
    
    # Build frontmatter
    frontmatter = {
        'type': 'post',
        'title': entry['title'],
        'date': pub_date.strftime('%Y-%m-%d %H:%M:%S'),
        'entry_id': extract_entry_id(entry['id']),
    }
    
    # Add original link if available
    if entry['link']:
        frontmatter['canonicalURL'] = entry['link']
    
    # Format frontmatter as YAML
    frontmatter_yaml = '---\n'
    for key, value in frontmatter.items():
        if isinstance(value, str) and (' ' in value or ':' in value):
            frontmatter_yaml += f'{key}: "{value}"\n'
        else:
            frontmatter_yaml += f'{key}: {value}\n'
    frontmatter_yaml += '---\n'
    
    # Write file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter_yaml)
        f.write('\n')
        f.write(markdown_content)
        f.write('\n')
    
    print(f"✓ Created: {filename}")
    return True


def main():
    """Main function to import posts from Atom feed."""
    script_dir = Path(__file__).parent
    feed_url = 'https://world.hey.com/joaoqalves/feed.atom'
    posts_dir = script_dir / 'content' / 'post'
    
    if not posts_dir.exists():
        posts_dir.mkdir(parents=True, exist_ok=True)
        print(f"Created posts directory: {posts_dir}")
    
    all_entries = []
    current_url = feed_url
    page = 1
    
    # Fetch all pages of the feed
    while current_url:
        print(f"\nFetching page {page}...")
        root, next_url = fetch_atom_feed(current_url)
        entries = parse_atom_feed(root)
        all_entries.extend(entries)
        print(f"Found {len(entries)} entries on page {page}")
        
        current_url = next_url
        page += 1
        
        # Safety limit to avoid infinite loops
        if page > 100:
            print("Warning: Reached page limit (100), stopping pagination")
            break
    
    print(f"\nTotal entries found: {len(all_entries)}\n")
    
    created = 0
    skipped = 0
    
    for entry in all_entries:
        if create_post_file(posts_dir, entry):
            created += 1
        else:
            skipped += 1
    
    print(f"\nSummary: {created} created, {skipped} skipped (already exist)")
    return 0


if __name__ == '__main__':
    exit(main())
