import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("div", None, [HTMLNode(value="Hello")], {"class": "greeting"})
        self.assertEqual(node.tag, "div")
        self.assertIsNone(node.value)
    
    def test_props_to_html(self):
        node = HTMLNode("a", "Click here", None, {"href": "www.example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="www.example.com" target="_blank"')
    
    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph.", None, {})
        self.assertEqual(repr(node), "HTMLNode(tag=p, value=This is a paragraph., children=[], props={})")
        
    #Testing leaf node (Reminder it should have NO children)
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
        
    def test_leaf_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
            
    def test_leaf_no_tag(self):
        node = LeafNode(None, "Just some text for Value")
        self.assertEqual(node.to_html(), "Just some text for Value")
        
    #Testing parent node (Reminder it should have NO value)
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_parent_no_tag(self):
        child_node = LeafNode("i", "italic text")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
            
    def test_parent_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()
            
    def test_parent_with_multiple_children(self):
        child1 = LeafNode("h1", "Title")
        child2 = LeafNode("p", "This is a paragraph.")
        parent_node = ParentNode("section", [child1, child2])
        self.assertEqual(
            parent_node.to_html(),
            "<section><h1>Title</h1><p>This is a paragraph.</p></section>",
        )
            
if __name__ == "__main__":
    unittest.main()