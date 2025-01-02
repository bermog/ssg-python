import re


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
