import unittest

from block_utilities import BlockType, block_to_block_type
from markdown_to_html import markdown_to_html_node
from textnode import TextNode, TextType

class TestMarkToHTML(unittest.TestCase):
    
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
also with a [link](www.example.com)
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here also with a <a href=\"www.example.com\">link</a></p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
        
    def test_unordered_list(self):
        md = """
- Item of unordered list
- There is no order
- Order up
- Sorry no order

This is the only paragraph with _italic_ text and `code` here
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item of unordered list</li><li>There is no order</li><li>Order up</li><li>Sorry no order</li></ul><p>This is the only paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
        
    def test_ordered_list(self):
        md = """
1. First item in list
2. Second item in list
3. Last item in list

Paragraph with **RANDOM** words for test
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item in list</li><li>Second item in list</li><li>Last item in list</li></ol><p>Paragraph with <b>RANDOM</b> words for test</p></div>",
        )
        
    def test_headers(self):
        md="""
#### Big header here

## Not so big header

# Baby header
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4>Big header here</h4><h2>Not so big header</h2><h1>Baby header</h1></div>",
        )