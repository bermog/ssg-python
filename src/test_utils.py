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

    def test_extract_markdown_links(self):
        text = """
            first url [to google](https://google.com) and another url
            [ddg](https://duckduckgo.com/)
        """
        expected = [
            ("to google", "https://google.com"),
            ("ddg", "https://duckduckgo.com/"),
        ]
        actual = Utils.extract_markdown_links(text)
        self.assertEqual(expected, actual)

    def test_extract_markdown_images(self):
        text = """
            here is a gif ![cat gif](https://imgur.com/NUyttbn) and another one
            ![squirrel gif](https://imgur.com/G9LgOkg)
        """
        expected = [
            ("cat gif", "https://imgur.com/NUyttbn"),
            ("squirrel gif", "https://imgur.com/G9LgOkg"),
        ]
        actual = Utils.extract_markdown_links(text)
        self.assertEqual(expected, actual)

    def test_split_nodes_link(self):
        node1 = TextNode(
            "[Google](https://google.com) and some text",
            TextType.NORMAL,
        )
        node2 = TextNode(
            "This is a link [to google](https://google.com) and some text",
            TextType.NORMAL,
        )
        node3 = TextNode(
            "This is a link [to google](https://google.com) and [to ddg](https://duckduckgo.com)",
            TextType.NORMAL,
        )
        expected = [
            TextNode("Google", TextType.LINK, "https://google.com"),
            TextNode(" and some text", TextType.NORMAL),
            TextNode("This is a link ", TextType.NORMAL),
            TextNode("to google", TextType.LINK, "https://google.com"),
            TextNode(" and some text", TextType.NORMAL),
            TextNode("This is a link ", TextType.NORMAL),
            TextNode("to google", TextType.LINK, "https://google.com"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to ddg", TextType.LINK, "https://duckduckgo.com"),
        ]
        actual = Utils.split_nodes_link([node1, node2, node3])
        self.assertEqual(expected, actual)

    def test_split_nodes_image(self):
        node1 = TextNode(
            "![Cat](https://imgur.com/NUyttbn) and some text",
            TextType.NORMAL,
        )
        node2 = TextNode(
            "This is ![a cat](https://imgur.com/NUyttbn) and some text",
            TextType.NORMAL,
        )
        node3 = TextNode(
            "This is ![a cat](https://imgur.com/NUyttbn) and ![a squirrel](https://imgur.com/G9LgOkg)",
            TextType.NORMAL,
        )
        expected = [
            TextNode("Cat", TextType.IMAGE, "https://imgur.com/NUyttbn"),
            TextNode(" and some text", TextType.NORMAL),
            TextNode("This is ", TextType.NORMAL),
            TextNode("a cat", TextType.IMAGE, "https://imgur.com/NUyttbn"),
            TextNode(" and some text", TextType.NORMAL),
            TextNode("This is ", TextType.NORMAL),
            TextNode("a cat", TextType.IMAGE, "https://imgur.com/NUyttbn"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("a squirrel", TextType.IMAGE, "https://imgur.com/G9LgOkg"),
        ]
        actual = Utils.split_nodes_image([node1, node2, node3])
        self.assertEqual(expected, actual)

    def test_text_to_textnodes(self):
        text = "This is **bold** text with *some italic* and a `code block`, with "
        text += "![a cat image](https://imgur.com/NUyttbn) and a "
        text += "[link to google](https://google.com)"
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text with ", TextType.NORMAL),
            TextNode("some italic", TextType.ITALIC),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(", with ", TextType.NORMAL),
            TextNode("a cat image", TextType.IMAGE, "https://imgur.com/NUyttbn"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link to google", TextType.LINK, "https://google.com"),
        ]
        actual = Utils.text_to_textnodes(text)
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
