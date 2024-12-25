import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_complete(self):
        node = LeafNode("a", "Click here", {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        expected = '<a href="https://www.google.com" target="_blank">Click here</a>'
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_to_html_props_missing(self):
        node = LeafNode("b", "Bold text")
        expected = "<b>Bold text</b>"
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_to_html_tag_missing(self):
        node = LeafNode(None, "Click here", {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        expected = "Click here"
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_to_html_value_missing(self):
        node = LeafNode("a", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertRaises(ValueError, node.to_html)
