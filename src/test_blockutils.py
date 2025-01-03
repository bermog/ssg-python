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

    def test_heading_markdown_to_html_node(self):
        markdown = "## This heading has **bold text** and more text"
        expected = "<div><h2>This heading has <b>bold text</b> and more text</h2></div>"
        actual = BlockUtils.markdown_to_html_node(markdown).to_html()
        self.assertEqual(expected, actual)

    def test_code_markdown_to_html_node(self):
        markdown = "```This is a code block```"
        expected = "<div><pre><code>This is a code block</code></pre></div>"
        actual = BlockUtils.markdown_to_html_node(markdown).to_html()
        self.assertEqual(expected, actual)

    def test_quote_markdown_to_html_node(self):
        markdown = ">This is a quote block"
        expected = "<div><blockquote>This is a quote block</blockquote></div>"
        actual = BlockUtils.markdown_to_html_node(markdown).to_html()
        self.assertEqual(expected, actual)

    def test_dash_unordered_list_markdown_to_html_node(self):
        markdown = "- First *item*\n"
        markdown += "- Second **item**\n"
        expected = """
            <div>
                <ul>
                    <li>First 
                        <i>item</i>
                    </li>
                    <li>Second 
                        <b>item</b>
                    </li>
                </ul>
            </div>
        """.replace(" ", "").replace("\n", "")
        actual = (
            BlockUtils.markdown_to_html_node(markdown)
            .to_html()
            .replace(" ", "")
            .replace("\n", "")
        )
        self.assertEqual(expected, actual)

    def test_star_unordered_list_markdown_to_html_node(self):
        markdown = "* First *item*\n"
        markdown += "* Second **item**\n"
        expected = """
            <div>
                <ul>
                    <li>First 
                        <i>item</i>
                    </li>
                    <li>Second 
                        <b>item</b>
                    </li>
                </ul>
            </div>
        """.replace(" ", "").replace("\n", "")
        actual = (
            BlockUtils.markdown_to_html_node(markdown)
            .to_html()
            .replace(" ", "")
            .replace("\n", "")
        )
        self.assertEqual(expected, actual)

    def test_ordered_list_markdown_to_html_node(self):
        markdown = "1. First *item*\n"
        markdown += "2. Second **item**\n"
        markdown += "3. Third `item`\n"
        expected = """
            <div>
                <ol>
                    <li>First 
                        <i>item</i>
                    </li>
                    <li>Second 
                        <b>item</b>
                    </li>
                    <li>Third 
                        <code>item</code>
                    </li>
                </ol>
            </div>
        """.replace(" ", "").replace("\n", "")
        actual = (
            BlockUtils.markdown_to_html_node(markdown)
            .to_html()
            .replace(" ", "")
            .replace("\n", "")
        )
        self.assertEqual(expected, actual)

    def test_paragraph_markdown_to_html_node(self):
        markdown = "This is a paragraph"
        expected = "<div><p>This is a paragraph</p></div>"
        actual = BlockUtils.markdown_to_html_node(markdown).to_html()
        self.assertEqual(expected, actual)

    def test_full_markdown_to_html_node(self):
        markdown = "### This is a header\n\n"
        markdown += "This is a paragraph with **bold text**\n"
        markdown += "and a second line here\n\n"
        markdown += "```\n"
        markdown += "This is a code block\n"
        markdown += "that continues here\n"
        markdown += "with a third line\n"
        markdown += "```\n\n"
        markdown += ">This is a quote with *italic text*\n\n"
        markdown += "- First unordered list item\n"
        markdown += "- Second unordered list item\n\n"
        markdown += "* Another unordered list\n"
        markdown += "* One more item\n\n"
        markdown += "1. First item of an ordered list\n"
        markdown += "2. Second item\n"
        expected = """
            <div>
                <h3>This is a header</h3>
                <p>This is a paragraph with 
                    <b>bold text</b>
                    and a second line here
                </p>
                <pre>
                    <code>
                        This is a code block
                        that continues here
                        with a third line
                    </code>
                </pre>
                <blockquote>This is a quote with 
                    <i>italic text</i>
                </blockquote>
                <ul>
                    <li>First unordered list item</li>
                    <li>Second unordered list item</li>
                </ul>
                <ul>
                    <li>Another unordered list</li>
                    <li>One more item</li>
                </ul>
                <ol>
                    <li>First item of an ordered list</li>
                    <li>Second item</li>
                </ol>
            </div>
        """.replace(" ", "").replace("\n", "")
        actual = (
            BlockUtils.markdown_to_html_node(markdown)
            .to_html()
            .replace(" ", "")
            .replace("\n", "")
        )
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
