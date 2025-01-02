import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_repr(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://test.dev")
        self.assertEqual(
            repr(node1),
            "TextNode(This is a text node, bold, https://test.dev)",
        )

        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(
            repr(node2),
            "TextNode(This is a text node, italic, None)",
        )

    def test_different_text(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Something else", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_different_type(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node1, node2)

    def test_different_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://test.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_normal_text_to_htmlnode(self):
        node = TextNode("Normal text", TextType.NORMAL)
        expected = "Normal text"
        actual = node.to_htmlnode().to_html()
        self.assertEqual(expected, actual)

    def test_bold_text_to_htmlnode(self):
        node = TextNode("Bold text", TextType.BOLD)
        expected = "<b>Bold text</b>"
        actual = node.to_htmlnode().to_html()
        self.assertEqual(expected, actual)

    def test_italic_text_to_htmlnode(self):
        node = TextNode("Italic text", TextType.ITALIC)
        expected = "<i>Italic text</i>"
        actual = node.to_htmlnode().to_html()
        self.assertEqual(expected, actual)

    def test_code_text_to_htmlnode(self):
        node = TextNode("Code text", TextType.CODE)
        expected = "<code>Code text</code>"
        actual = node.to_htmlnode().to_html()
        self.assertEqual(expected, actual)

    def test_link_text_to_htmlnode(self):
        node = TextNode("Link text", TextType.LINK, "https://google.com")
        expected = '<a href="https://google.com">Link text</a>'
        actual = node.to_htmlnode().to_html()
        self.assertEqual(expected, actual)

    def test_image_text_to_htmlnode(self):
        node = TextNode("Image text", TextType.IMAGE, "myImage.png")
        expected = '<img src="myImage.png" alt="Image text"></img>'
        actual = node.to_htmlnode().to_html()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
