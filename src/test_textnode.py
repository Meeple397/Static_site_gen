import unittest


from textnode import TextNode, TextType, text_node_to_html_node




class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
       
        node2 = TextNode("This is a bold text node", TextType.BOLD)
        html_node2 = text_node_to_html_node(node2)
        self.assertEqual(html_node2.tag, "b")
        self.assertEqual(html_node2.value, "This is a bold text node")


        node3 = TextNode("This is an italic text node", TextType.ITALIC)
        html_node3 = text_node_to_html_node(node3)
        self.assertEqual(html_node3.tag, "i")
        self.assertEqual(html_node3.value, "This is an italic text node")


        node4 = TextNode("This is a code text node", TextType.CODE)
        html_node4 = text_node_to_html_node(node4)
        self.assertEqual(html_node4.tag, "code")
        self.assertEqual(html_node4.value, "This is a code text node")


        node5 = TextNode("This is a link text node", TextType.LINK, "https://www.umass.edu/it/canvas")
        html_node5 = text_node_to_html_node(node5)
        self.assertEqual(html_node5.tag, "a")
        self.assertEqual(html_node5.value, "This is a link text node")
        self.assertEqual(html_node5.props, {"href": "https://www.umass.edu/it/canvas"})


        node6 = TextNode("This is an image text node", TextType.IMAGE, "https://www.umass.edu/it/canvas")
        html_node6 = text_node_to_html_node(node6)
        self.assertEqual(html_node6.tag, "img")
        self.assertEqual(html_node6.value, "")
        self.assertEqual(html_node6.props, {"src": "https://www.umass.edu/it/canvas", "alt": "This is an image text node"})




if __name__ == "__main__":
    unittest.main()
