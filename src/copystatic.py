import os
import shutil


def copy_directory_contents(source, destination):
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
            copy_directory_contents(source_path, destination_path)
    else:
        shutil.copy(source, destination)
