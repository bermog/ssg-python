#!/usr/bin/env python3

from ssg import SSG

path_static = "./static"
path_content = "./content"
path_template = "./template.html"
path_public = "./public"


def main():
    generator = SSG(path_static, path_content, path_template, path_public)

    print("Generating public content")
    generator.generate_website()
    print("Done")


if __name__ == "__main__":
    main()
