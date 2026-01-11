import os
import json
from django.conf import settings


class FileHandler:
    """
    Read / write file
    """

    def __init__(self, base_dir=None) -> None:
        if isinstance(base_dir, str):
            self.base_dir = base_dir
        else:
            self.base_dir = settings.BASE_DIR

    def file_path(self, file_name, add_path=None):
        if isinstance(add_path, list):
            path = os.path.join(self.base_dir, *add_path, file_name)
        elif isinstance(add_path, str):
            path = os.path.join(self.base_dir, add_path, file_name)
        else:
            path = os.path.join(self.base_dir, file_name)
        return path

    def read_json(self, file_name, mode, add_path=None):
        """
        read json file : r/r+/rb
        write json file: w/w+/wb
        """
        # file path
        path = self.file_path(file_name, add_path)

        with open(path, mode) as f:
            data = json.load(f)
        return data

    def write_json(self, file_name, mode, content, add_path=None):
        """
        read json file : r/r+/rb
        write json file: w/w+/wb
        """
        # file path
        path = self.file_path(file_name, add_path)

        with open(path, mode) as f:
            json.dump(content, f)
        return True

    def rw_file(self, file_name, mode, content=None, add_path=None):
        """
        read file : r/r+/rb
        write file: w/w+/wb
        """
        # file path
        path = self.file_path(file_name, add_path)

        # read/write append
        if mode in "r":
            with open(path, mode) as f:
                data = f.read()
        else:
            with open(path, mode) as f:
                data = f.write(content)
        return data
