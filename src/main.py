#!/usr/bin/env python3

from copystatic import copy_directory_contents

path_static = "./static"
path_public = "./public"


def main():
    print("Generating public content")
    copy_directory_contents(path_static, path_public)
    print("Done")


if __name__ == "__main__":
    main()
