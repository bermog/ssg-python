import unittest

from blockutils import BlockType, BlockUtils


class TestBlockUtils(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "  # This is a heading\n\n    "
        markdown += (
            "      This is a paragraph with **bold** and *italic* words.   \n\n\n"
        )
        markdown += "* This is the first item in a list\n"
        markdown += "* This is another item\n"
        markdown += "* This is the last item    \n\n"
        expected = [
            "# This is a heading",
            "This is a paragraph with **bold** and *italic* words.",
            "* This is the first item in a list\n"
            + "* This is another item\n"
            + "* This is the last item",
        ]
        actual = BlockUtils.markdown_to_blocks(markdown)
        self.assertEqual(expected, actual)

    def test_heading_block_to_block_type(self):
        block1 = "# text"
        block2 = "###### text"
        expected = BlockType.HEADING
        actual = BlockUtils.block_to_block_type(block1)
        self.assertEqual(expected, actual)
        actual = BlockUtils.block_to_block_type(block2)
        self.assertEqual(expected, actual)

        block3 = "#text"
        block4 = "#-# text"
        expected = BlockType.PARAGRAPH
        actual = BlockUtils.block_to_block_type(block3)
        self.assertEqual(expected, actual)
        actual = BlockUtils.block_to_block_type(block4)
        self.assertEqual(expected, actual)

    def test_code_block_to_block_type(self):
        block1 = "```text```"
        block2 = "```python\ncode here\n```"
        expected = BlockType.CODE
        actual = BlockUtils.block_to_block_type(block1)
        self.assertEqual(expected, actual)
        actual = BlockUtils.block_to_block_type(block2)
        self.assertEqual(expected, actual)

        block3 = "``text```"
        block4 = "```python\ncode here\n`"
        expected = BlockType.PARAGRAPH
        actual = BlockUtils.block_to_block_type(block3)
        self.assertEqual(expected, actual)
        actual = BlockUtils.block_to_block_type(block4)
        self.assertEqual(expected, actual)

    def test_quote_block_to_block_type(self):
        block1 = ">quote"
        expected = BlockType.QUOTE
        actual = BlockUtils.block_to_block_type(block1)
        self.assertEqual(expected, actual)

        block2 = "a>quote"
        expected = BlockType.PARAGRAPH
        actual = BlockUtils.block_to_block_type(block2)
        self.assertEqual(expected, actual)

    def test_unordered_list_block_to_block_type(self):
        block1 = "* text"
        block2 = "- text"
        expected = BlockType.UNORDERED_LIST
        actual = BlockUtils.block_to_block_type(block1)
        self.assertEqual(expected, actual)
        actual = BlockUtils.block_to_block_type(block2)
        self.assertEqual(expected, actual)

        block3 = "*text"
        block4 = "-text"
        expected = BlockType.PARAGRAPH
        actual = BlockUtils.block_to_block_type(block3)
        self.assertEqual(expected, actual)
        actual = BlockUtils.block_to_block_type(block4)
        self.assertEqual(expected, actual)

    def test_ordered_list_block_to_block_type(self):
        block1 = "1. text"
        block2 = "100. text"
        expected = BlockType.ORDERED_LIST
        actual = BlockUtils.block_to_block_type(block1)
        self.assertEqual(expected, actual)
        actual = BlockUtils.block_to_block_type(block2)
        self.assertEqual(expected, actual)

        block3 = "1.text"
        block4 = "1000.text"
        expected = BlockType.PARAGRAPH
        actual = BlockUtils.block_to_block_type(block3)
        self.assertEqual(expected, actual)
        actual = BlockUtils.block_to_block_type(block4)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
