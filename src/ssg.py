import os
from blockutils import BlockUtils


class SSG:
    @staticmethod
    def generate_page(path_source, path_template, path_destination):
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
