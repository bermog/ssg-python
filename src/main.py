#!/usr/bin/env python3

from ssg import SSG
from copystatic import copy_directory_contents

path_static = "./static"
path_public = "./public"


def main():
    print("Generating public content")
    copy_directory_contents(path_static, path_public)
    SSG.generate_pages_recursive("./content", "./template.html", "./public")
    print("Done")


if __name__ == "__main__":
    main()
