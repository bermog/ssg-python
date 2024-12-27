import re

from leafnode import LeafNode
from textnode import TextNode, TextType


class Utils:
    @staticmethod
    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.NORMAL:
                return LeafNode(None, text_node.text)
            case TextType.BOLD:
                return LeafNode("b", text_node.text)
            case TextType.ITALIC:
                return LeafNode("i", text_node.text)
            case TextType.CODE:
                return LeafNode("code", text_node.text)
            case TextType.LINK:
                return LeafNode("a", text_node.text, {"href": text_node.url})
            case TextType.IMAGE:
                return LeafNode(
                    "img", "", {"src": text_node.url, "alt": text_node.text}
                )
            case _:
                raise Exception("Invalid TextNode type")

    @staticmethod
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        # Delimiter will be used in a regex, so we must escape all "*"
        if "*" in delimiter:
            delimiter = "".join(map(lambda d: f"\\{d}", delimiter))

        new_nodes = []
        for node in old_nodes:
            # Use regex to handle different delimiters using the same character
            # (e.g. handle italic (*) separately from bold (**))
            regex = f"(?<!{delimiter}){delimiter}(?!{delimiter})"
            split_text = re.split(regex, node.text)
            for text in split_text:
                if len(text) > 0:
                    node_type = (
                        node.text_type if split_text.index(text) % 2 == 0 else text_type
                    )
                    new_nodes.append(TextNode(text, node_type))

        return new_nodes
