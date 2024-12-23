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


if __name__ == "__main__":
    unittest.main()
