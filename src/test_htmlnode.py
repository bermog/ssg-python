import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", None, None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        expected = ' href="https://www.google.com" target="_blank"'
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

    def test_repr(self):
        node1 = HTMLNode("a", "Click this", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        node2 = HTMLNode("p", "Text in a paragraph", [node1], {
            "text-align": "right",
        })
        node3 = HTMLNode("p", "Another paragraph", None, {
            "text-align": "left",
            "color": "navy",
        })
        node4 = HTMLNode("div", None, [node2, node3], {
            "background-color": "blue"
        })

        expected = """
          * HTMLNode: div - None
            * HTMLNode: p - Text in a paragraph
              * HTMLNode: a - Click this
                href: https://www.google.com
                target: _blank
              text-align: right
            * HTMLNode: p - Another paragraph
              text-align: left
              color: navy
            background-color: blue
        """.replace(" ", "").replace("\n", "")
        actual = repr(node4).replace(" ", "").replace("\n", "")

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
