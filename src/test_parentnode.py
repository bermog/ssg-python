import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_leaf_children(self):
        node1 = LeafNode("b", "Bold text", None)
        node2 = LeafNode("i", "Italic text", None)
        node3 = ParentNode("div", [node1, node2], None)

        expected = "<div><b>Bold text</b><i>Italic text</i></div>"
        actual = node3.to_html()
        self.assertEqual(expected, actual)

    def test_to_html_hybrid_children(self):
        node1 = LeafNode("span", "Bold text", {"style": "color:white;font-weight:bold"})
        node2 = LeafNode("a", "Click here", {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        node3 = ParentNode("div", [node1, node2], {"style": "background-color:teal"})
        node4 = LeafNode("span", "Pink background", {"style": "background-color:pink"})
        node5 = ParentNode("div", [node3, node4], None)

        expected = """
          <div>
            <div style="background-color:teal">
                <span style="color:white;font-weight:bold">Bold text</span>
                <a href="https://www.google.com" target="_blank">Click here</a>
            </div>
            <span style="background-color:pink">Pink background</span>
          </div>
        """.replace(" ", "").replace("\n", "")
        actual = node5.to_html().replace(" ", "").replace("\n", "")
        self.assertEqual(expected, actual)
