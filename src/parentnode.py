from functools import reduce

from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag missing from ParentNode")
        if self.children is None:
            raise ValueError("Children missing from ParentNode")

        html = f"<{self.tag}{self.props_to_html()}>"
        html += reduce(
            lambda html_so_far, child: html_so_far + child.to_html(), self.children, ""
        )
        html += f"</{self.tag}>"
        return html

    def get_child_html(self):
        if self.children is None:
            return ""

        html = ""
        for child in self.children:
            html += child.to_html()
