import unittest

from textnode import TextNode, TextType
from inlineutils import InlineUtils


class TestInlineUtils(unittest.TestCase):
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
        actual = InlineUtils.text_to_textnodes(text)
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
        actual = InlineUtils.split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
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
        actual = InlineUtils.split_nodes_delimiter([node1, node2], "*", TextType.ITALIC)
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
        actual = InlineUtils.split_nodes_delimiter([node1, node2], "`", TextType.CODE)
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
        actual = InlineUtils.extract_markdown_links(text)
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
        actual = InlineUtils.extract_markdown_links(text)
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
        actual = InlineUtils.split_nodes_link([node1, node2, node3])
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
        actual = InlineUtils.split_nodes_image([node1, node2, node3])
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
