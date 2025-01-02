import re
from enum import Enum


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
