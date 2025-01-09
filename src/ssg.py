import os
import shutil
from blockutils import BlockUtils


class SSG:
    def __init__(self, path_static, path_content, path_template, path_public):
        self.path_static = path_static
        self.path_content = path_content
        self.path_template = path_template
        self.path_public = path_public

    def generate_website(self):
        self.__copy_directory_contents(self.path_static, self.path_public)
        self.__generate_pages_recursive(
            self.path_content, self.path_template, self.path_public
        )

    def __copy_directory_contents(self, source, destination):
        if not os.path.exists(source):
            raise Exception(f"Copy source could not be found: {source}")

        if os.path.exists(destination):
            print(f"Overwriting the existing {destination} directory")
            shutil.rmtree(destination)

        if os.path.isdir(source):
            os.mkdir(destination)
            contents = os.listdir(source)
            for item in contents:
                source_path = os.path.join(source, item)
                destination_path = os.path.join(destination, item)
                self.__copy_directory_contents(source_path, destination_path)
        else:
            shutil.copy(source, destination)

    def __generate_page(self, path_source, path_template, path_destination):
        print(
            f"Generating page from {path_source} to {path_destination} using {path_template}"
        )

        markdown = None
        template = None
        with open(path_source) as s:
            markdown = s.read()
        with open(path_template) as t:
            template = t.read()

        title = BlockUtils.extract_title(markdown)
        content = BlockUtils.markdown_to_html_node(markdown).to_html()
        html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

        dir_destination = os.path.dirname(path_destination)
        if not os.path.exists(dir_destination):
            os.makedirs(dir_destination)

        html_file = open(path_destination, "w")
        html_file.write(html)
        html_file.close()

    def __generate_pages_recursive(
        self, dir_path_source, path_template, dir_path_destination
    ):
        if not os.path.exists(dir_path_source):
            raise Exception(f"Copy source could not be found: {dir_path_source}")

        if os.path.isdir(dir_path_source):
            contents = os.listdir(dir_path_source)
            for item in contents:
                source_path = os.path.join(dir_path_source, item)
                destination_path = os.path.join(dir_path_destination, item)
                self.__generate_pages_recursive(
                    source_path, path_template, destination_path
                )
        else:
            if dir_path_source.endswith(r".md"):
                destination = dir_path_destination.replace("md", "html")
                self.__generate_page(dir_path_source, path_template, destination)
            else:
                shutil.copy(dir_path_source, dir_path_destination)
