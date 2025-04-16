import unittest


from htmlnode import HTMLNode, LeafNode, ParentNode




class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a test", ["s"], {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p", "This is a test, 2", ["AbracaDaniel"], {"href": "https://www.umass.edu/it/canvas", "target": "_blank"})
        node3 = HTMLNode("a", "This is drill")
        node.props_to_html()
        node2.__repr__()
        node3.__repr__()
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')


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




if __name__ == "__main__":
    unittest.main()