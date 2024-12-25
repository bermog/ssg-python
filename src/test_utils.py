import unittest

from textnode import TextNode, TextType
from utils import Utils


class TestUtils(unittest.TestCase):
    def test_normal_text_to_html_node(self):
        node = TextNode("Normal text", TextType.NORMAL)
        expected = "Normal text"
        actual = Utils.text_node_to_html_node(node).to_html()
        self.assertEqual(expected, actual)

    def test_bold_text_to_html_node(self):
        node = TextNode("Bold text", TextType.BOLD)
        expected = "<b>Bold text</b>"
        actual = Utils.text_node_to_html_node(node).to_html()
        self.assertEqual(expected, actual)

    def test_italic_text_to_html_node(self):
        node = TextNode("Italic text", TextType.ITALIC)
        expected = "<i>Italic text</i>"
        actual = Utils.text_node_to_html_node(node).to_html()
        self.assertEqual(expected, actual)

    def test_code_text_to_html_node(self):
        node = TextNode("Code text", TextType.CODE)
        expected = "<code>Code text</code>"
        actual = Utils.text_node_to_html_node(node).to_html()
        self.assertEqual(expected, actual)

    def test_link_text_to_html_node(self):
        node = TextNode("Link text", TextType.LINK, "https://google.com")
        expected = '<a href="https://google.com">Link text</a>'
        actual = Utils.text_node_to_html_node(node).to_html()
        self.assertEqual(expected, actual)

    def test_image_text_to_html_node(self):
        node = TextNode("Image text", TextType.IMAGE, "myImage.png")
        expected = '<img src="myImage.png" alt="Image text"></img>'
        actual = Utils.text_node_to_html_node(node).to_html()
        self.assertEqual(expected, actual)
