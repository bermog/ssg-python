#!/usr/bin/env python3

from textnode import TextNode, TextType


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
    print(node)

main()
