import re
from itertools import zip_longest

from textnode import TextNode, TextType


class InlineUtils:
    @staticmethod
    def text_to_textnodes(text):
        text_node = TextNode(text, TextType.NORMAL)
        output = InlineUtils.split_nodes_delimiter([text_node], "*", TextType.ITALIC)
        output = InlineUtils.split_nodes_delimiter(output, "**", TextType.BOLD)
        output = InlineUtils.split_nodes_delimiter(output, "`", TextType.CODE)
        output = InlineUtils.split_nodes_image(output)
        output = InlineUtils.split_nodes_link(output)
        return output

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

    @staticmethod
    def extract_markdown_links(text):
        regex = r"\[.+?\]\(.+?\)"
        links = re.findall(regex, text)
        results = []
        for link in links:
            anchor_text = link.split("[")[1].split("]")[0]
            url = link.split("(")[1].split(")")[0]
            results.append((anchor_text, url))
        return results

    @staticmethod
    def extract_markdown_images(text):
        regex = r"\!\[.+?\]\(.+?\)"
        images = re.findall(regex, text)
        results = []
        for image in images:
            alt_text = image.split("[")[1].split("]")[0]
            url = image.split("(")[1].split(")")[0]
            results.append((alt_text, url))
        return results

    @staticmethod
    def split_nodes_link(old_nodes):
        regex = r"\[.+?\]\(.+?\)"
        new_nodes = []
        for node in old_nodes:
            split_text = re.split(regex, node.text)
            links = InlineUtils.extract_markdown_links(node.text)
            for text, link in zip_longest(split_text, links):
                if text is not None and len(text) > 0:
                    new_nodes.append(TextNode(text, node.text_type, node.url))
                if link is not None:
                    new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
        return new_nodes

    @staticmethod
    def split_nodes_image(old_nodes):
        regex = r"\!\[.+?\]\(.+?\)"
        new_nodes = []
        for node in old_nodes:
            split_text = re.split(regex, node.text)
            images = InlineUtils.extract_markdown_images(node.text)
            for text, image in zip_longest(split_text, images):
                if text is not None and len(text) > 0:
                    new_nodes.append(TextNode(text, node.text_type, node.url))
                if image is not None:
                    new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
        return new_nodes
