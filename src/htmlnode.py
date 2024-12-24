from functools import reduce


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is not None:
            return reduce(
                lambda html, prop: f'{html} {prop[0]}="{prop[1]}"',
                self.props.items(),
                "",
            )
        return ""

    def pretty_print(self, indent_level=1):
        indent = "  " * indent_level
        description = f"{indent}* HTMLNode: {self.tag} - {self.value}"
        indent += "  "

        if self.children is not None:
            description += reduce(
                lambda children,
                child: f"{children}{indent}\n{child.pretty_print(indent_level + 1)}",
                self.children,
                indent,
            )

        if self.props is not None:
            description += reduce(
                lambda props, prop: f"{props}\n{indent}{prop[0]}: {prop[1]}",
                self.props.items(),
                indent,
            )

        return description

    def __repr__(self):
        return self.pretty_print()
