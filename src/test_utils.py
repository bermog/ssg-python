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

    def test_markdown_to_blocks(self):
        markdown = "  # This is a heading\n\n    "
        markdown += "      This is a paragraph with **bold** and *italic* words.   \n\n\n"
        markdown += "* This is the first item in a list\n"
        markdown += "* This is another item\n"
        markdown += "* This is the last item    \n\n"
        expected = [
            "# This is a heading",
            "This is a paragraph with **bold** and *italic* words.",
            "* This is the first item in a list\n" +
            "* This is another item\n" +
            "* This is the last item"
        ]
        actual = Utils.markdown_to_blocks(markdown)
        self.assertEqual(expected, actual)

    def test_heading_block_to_block_type(self):
        block1 = "# text"
        block2 = "###### text"
        expected = "heading"
        actual = Utils.block_to_block_type(block1)
        self.assertEqual(expected, actual)
        actual = Utils.block_to_block_type(block2)
        self.assertEqual(expected, actual)

        block3 = "#text"
        block4 = "#-# text"
        expected = "paragraph"
        actual = Utils.block_to_block_type(block3)
        self.assertEqual(expected, actual)
        actual = Utils.block_to_block_type(block4)
        self.assertEqual(expected, actual)

    def test_code_block_to_block_type(self):
        block1 = "```text```"
        block2 = "```python\ncode here\n```"
        expected = "code"
        actual = Utils.block_to_block_type(block1)
        self.assertEqual(expected, actual)
        actual = Utils.block_to_block_type(block2)
        self.assertEqual(expected, actual)

        block3 = "``text```"
        block4 = "```python\ncode here\n`"
        expected = "paragraph"
        actual = Utils.block_to_block_type(block3)
        self.assertEqual(expected, actual)
        actual = Utils.block_to_block_type(block4)
        self.assertEqual(expected, actual)

    def test_quote_block_to_block_type(self):
        block1 = ">quote"
        expected = "quote"
        actual = Utils.block_to_block_type(block1)
        self.assertEqual(expected, actual)

        block2 = "a>quote"
        expected = "paragraph"
        actual = Utils.block_to_block_type(block2)
        self.assertEqual(expected, actual)

    def test_unordered_list_block_to_block_type(self):
        block1 = "* text"
        block2 = "- text"
        expected = "unordered_list"
        actual = Utils.block_to_block_type(block1)
        self.assertEqual(expected, actual)
        actual = Utils.block_to_block_type(block2)
        self.assertEqual(expected, actual)

        block3 = "*text"
        block4 = "-text"
        expected = "paragraph"
        actual = Utils.block_to_block_type(block3)
        self.assertEqual(expected, actual)
        actual = Utils.block_to_block_type(block4)
        self.assertEqual(expected, actual)

    def test_ordered_list_block_to_block_type(self):
        block1 = "1. text"
        block2 = "100. text"
        expected = "ordered_list"
        actual = Utils.block_to_block_type(block1)
        self.assertEqual(expected, actual)
        actual = Utils.block_to_block_type(block2)
        self.assertEqual(expected, actual)

        block3 = "1.text"
        block4 = "1000.text"
        expected = "paragraph"
        actual = Utils.block_to_block_type(block3)
        self.assertEqual(expected, actual)
        actual = Utils.block_to_block_type(block4)
        self.assertEqual(expected, actual)
