import pytest
import os
from html.parser import HTMLParser

class AnchorAndIdParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.anchor_links = []

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

def test_anchor_links_have_targets():
    """
    Parses index.html to ensure all internal anchor links (e.g. href="#contact")
    have a matching element with that ID (e.g. id="contact").
    """
    index_path = os.path.join(os.path.dirname(__file__), '..', 'index.html')

    assert os.path.exists(index_path), "index.html does not exist in the root directory"

    with open(index_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    parser = AnchorAndIdParser()
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

    parser = AnchorAndIdParser()
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

    parser = AnchorAndIdParser()
    parser.feed(html_content)

    assert 'contact-form' in parser.ids, "Contact form (id='contact-form') is missing."
    assert 'form-success' in parser.ids, "Form success message (id='form-success') is missing."
