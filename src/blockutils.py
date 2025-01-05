import re
from enum import Enum

from inlineutils import InlineUtils
from parentnode import ParentNode


class BlockType(Enum):
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    PARAGRAPH = "paragraph"


class BlockUtils:
    @staticmethod
    def markdown_to_blocks(markdown):
        blocks = markdown.split("\n\n")
        blocks = list(map(lambda block: block.strip(), blocks))
        blocks = list(filter(lambda block: len(block) > 0, blocks))
        return blocks

    @staticmethod
    def block_to_block_type(block):
        if len(re.findall(r"^#{1,6} ", block)) > 0:
            return BlockType.HEADING
        elif block.startswith("```") and block.endswith("```"):
            return BlockType.CODE
        elif block.startswith(">"):
            return BlockType.QUOTE
        elif block.startswith("* ") or block.startswith("- "):
            return BlockType.UNORDERED_LIST
        elif len(re.findall(r"^\d+\. ", block)) > 0:
            return BlockType.ORDERED_LIST
        else:
            return BlockType.PARAGRAPH

    @staticmethod
    def block_to_heading(block):
        hashtag_amount = len(block.split()[0])
        text = block.split("# ")[1] if hashtag_amount in range(1, 7) else block
        children = InlineUtils.text_to_htmlnodes(text)
        return ParentNode(f"h{hashtag_amount}", children)

    @staticmethod
    def block_to_code(block):
        # TODO: Consider implementing the HTML5 class that specifies language
        # (e.g. "```python" should become '<code class="language-python">'
        text = block.split("```")[1].strip()
        children = InlineUtils.text_to_htmlnodes(text)
        return ParentNode("pre", [ParentNode("code", children)])

    @staticmethod
    def block_to_blockquote(block):
        text = block.split(">")[1].strip()
        children = InlineUtils.text_to_htmlnodes(text)
        return ParentNode("blockquote", children)

    @staticmethod
    def block_to_list(markdown, block_type):
        regex = None
        list_tag = None

        match block_type:
            case BlockType.UNORDERED_LIST:
                regex = r"^(\*|-) "
                list_tag = "ul"
            case BlockType.ORDERED_LIST:
                regex = r"^\d+\. "
                list_tag = "ol"
            case _:
                raise ValueError(f"Unable to convert {block_type} to HTML list")

        items = markdown.split("\n")
        items = list(map(lambda item: re.split(regex, item)[-1], items))
        items = list(filter(lambda item: len(item) > 0, items))
        items = list(map(lambda item: item.strip(), items))
        children = list(
            map(
                lambda item: ParentNode("li", InlineUtils.text_to_htmlnodes(item)),
                items,
            )
        )
        return ParentNode(list_tag, children)

    @staticmethod
    def block_to_paragraph(block):
        children = InlineUtils.text_to_htmlnodes(block)
        return ParentNode("p", children)

    @staticmethod
    def block_to_htmlnode(block, block_type):
        match block_type:
            case BlockType.HEADING:
                return BlockUtils.block_to_heading(block)
            case BlockType.CODE:
                return BlockUtils.block_to_code(block)
            case BlockType.QUOTE:
                return BlockUtils.block_to_blockquote(block)
            case BlockType.UNORDERED_LIST:
                return BlockUtils.block_to_list(block, block_type)
            case BlockType.ORDERED_LIST:
                return BlockUtils.block_to_list(block, block_type)
            case BlockType.PARAGRAPH:
                return BlockUtils.block_to_paragraph(block)
            case _:
                raise ValueError(f"Invalid markdown block type: {block_type}")

    @staticmethod
    def markdown_to_html_node(markdown):
        blocks = BlockUtils.markdown_to_blocks(markdown)
        children = []

        for block in blocks:
            block_type = BlockUtils.block_to_block_type(block)
            node = BlockUtils.block_to_htmlnode(block, block_type)
            children.append(node)

        return ParentNode("div", children)

    @staticmethod
    def extract_title(markdown):
        regex = r"^#{1} .+"
        match = re.findall(regex, markdown, re.MULTILINE)
        if len(match) > 0:
            return match[0].split("# ")[-1]
        raise Exception("Title not found in markdown (e.g. '# My title')")
