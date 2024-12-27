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

    def test_bold_split_nodes_delimiter(self):
        node1 = TextNode("Some **bold text here** and more text", TextType.NORMAL)
        node2 = TextNode("**Bold text** and **more bold text**", TextType.NORMAL)
        expected = [
            TextNode("Some ", TextType.NORMAL),
            TextNode("bold text here", TextType.BOLD),
            TextNode(" and more text", TextType.NORMAL),
            TextNode("Bold text", TextType.BOLD),
            TextNode(" and ", TextType.NORMAL),
            TextNode("more bold text", TextType.BOLD),
        ]
        actual = Utils.split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
        self.assertEqual(expected, actual)

    def test_italic_split_nodes_delimiter(self):
        node1 = TextNode("Some *italic text here* and more text", TextType.NORMAL)
        node2 = TextNode("*Italic text* and *more italic text*", TextType.NORMAL)
        expected = [
            TextNode("Some ", TextType.NORMAL),
            TextNode("italic text here", TextType.ITALIC),
            TextNode(" and more text", TextType.NORMAL),
            TextNode("Italic text", TextType.ITALIC),
            TextNode(" and ", TextType.NORMAL),
            TextNode("more italic text", TextType.ITALIC),
        ]
        actual = Utils.split_nodes_delimiter([node1, node2], "*", TextType.ITALIC)
        self.assertEqual(expected, actual)

    def test_code_split_nodes_delimiter(self):
        node1 = TextNode("Some `code here` and more text", TextType.NORMAL)
        node2 = TextNode("`Code` and `more code`", TextType.NORMAL)
        expected = [
            TextNode("Some ", TextType.NORMAL),
            TextNode("code here", TextType.CODE),
            TextNode(" and more text", TextType.NORMAL),
            TextNode("Code", TextType.CODE),
            TextNode(" and ", TextType.NORMAL),
            TextNode("more code", TextType.CODE),
        ]
        actual = Utils.split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        self.assertEqual(expected, actual)
