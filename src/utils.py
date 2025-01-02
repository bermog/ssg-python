import re

from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextType


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
    def markdown_to_blocks(markdown):
        blocks = markdown.split("\n\n")
        blocks = list(map(lambda block: block.strip(), blocks))
        blocks = list(filter(lambda block: len(block) > 0, blocks))
        return blocks

    @staticmethod
    def block_to_block_type(block):
        if len(re.findall(r"^#{1,6} ", block)) > 0:
            return "heading"
        elif block.startswith("```") and block.endswith("```"):
            return "code"
        elif block.startswith(">"):
            return "quote"
        elif block.startswith("* ") or block.startswith("- "):
            return "unordered_list"
        elif len(re.findall(r"^\d+\. ", block)) > 0:
            return "ordered_list"
        else:
            return "paragraph"
