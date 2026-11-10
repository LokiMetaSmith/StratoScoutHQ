import pytest
import os
from html.parser import HTMLParser

class EnhancedHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.anchor_links = []
        self.img_tags = []
        self.section_tags = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)

        # Collect IDs
        if 'id' in attr_dict:
            self.ids.add(attr_dict['id'])

        # Collect anchor links (href starting with #)
        if tag == 'a' and 'href' in attr_dict:
            href = attr_dict['href']
            if href.startswith('#') and len(href) > 1:
                self.anchor_links.append(href[1:]) # Store without the #

        # Collect img tags
        if tag == 'img':
            self.img_tags.append(attr_dict)

        # Collect section tags
        if tag == 'section':
            self.section_tags.append(attr_dict)

def test_anchor_links_have_targets():
    """
    Parses index.html to ensure all internal anchor links (e.g. href="#contact")
    have a matching element with that ID (e.g. id="contact").
    """
    index_path = os.path.join(os.path.dirname(__file__), '..', 'index.html')

    assert os.path.exists(index_path), "index.html does not exist in the root directory"

    with open(index_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    parser = EnhancedHTMLParser()
    parser.feed(html_content)

    # Assert that every anchor link target exists as an ID in the document
    for link_id in parser.anchor_links:
        assert link_id in parser.ids, f"Anchor link target '#{link_id}' not found as an ID in the HTML document."

def test_demo_and_validation_sections_exist():
    """
    Parses index.html to ensure the demo and validation sections exist.
    """
    index_path = os.path.join(os.path.dirname(__file__), '..', 'index.html')

    with open(index_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    parser = EnhancedHTMLParser()
    parser.feed(html_content)

    assert 'demo' in parser.ids, "Demo section (id='demo') is missing."
    assert 'validation' in parser.ids, "Validation section (id='validation') is missing."

def test_contact_form_exists():
    """
    Parses index.html to ensure the contact form and form success elements exist.
    """
    index_path = os.path.join(os.path.dirname(__file__), '..', 'index.html')

    with open(index_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    parser = EnhancedHTMLParser()
    parser.feed(html_content)

    assert 'contact-form' in parser.ids, "Contact form (id='contact-form') is missing."
    assert 'form-success' in parser.ids, "Form success message (id='form-success') is missing."

def test_analytics_script_exists():
    """
    Parses index.html to ensure the analytics tracking placeholder exists.
    """
    index_path = os.path.join(os.path.dirname(__file__), '..', 'index.html')

    with open(index_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    parser = EnhancedHTMLParser()
    parser.feed(html_content)

    assert 'analytics-script' in parser.ids, "Analytics script placeholder (id='analytics-script') is missing."

def test_demo_video_container_exists():
    """
    Parses index.html to ensure the demo video embed placeholder exists.
    """
    index_path = os.path.join(os.path.dirname(__file__), '..', 'index.html')

    with open(index_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    parser = EnhancedHTMLParser()
    parser.feed(html_content)

    assert 'demo-video-container' in parser.ids, "Demo video embed placeholder (id='demo-video-container') is missing."

def test_img_tags_have_alt_attributes():
    """
    Parses index.html to ensure all <img> tags have an 'alt' attribute.
    """
    index_path = os.path.join(os.path.dirname(__file__), '..', 'index.html')

    with open(index_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    parser = EnhancedHTMLParser()
    parser.feed(html_content)

    for i, img_attrs in enumerate(parser.img_tags):
        assert 'alt' in img_attrs, f"<img> tag at index {i} is missing an 'alt' attribute."

def test_section_tags_have_id_attributes():
    """
    Parses index.html to ensure all <section> tags have an 'id' attribute,
    which is required by the JavaScript scroll tracking to function without errors.
    """
    index_path = os.path.join(os.path.dirname(__file__), '..', 'index.html')

    with open(index_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    parser = EnhancedHTMLParser()
    parser.feed(html_content)

    for i, section_attrs in enumerate(parser.section_tags):
        assert 'id' in section_attrs, f"<section> tag at index {i} is missing an 'id' attribute."
