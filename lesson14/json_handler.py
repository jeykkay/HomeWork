from base_handler import BaseHandler
import json


class JsonHandler(BaseHandler):
    def __init__(self, path):
        self._path = path
        self.file = None

    @property
    def path(self):
        return self._path

    def read_file(self):
        self.file = open(self._path, 'r')
        return self.file.read()

    def append(self, content):
        with open(self._path, 'r') as file:
            file_content = json.load(file)
        if not isinstance(file_content, list):
            raise TypeError('Must be a list format')
        else:
            file = open(self._path)
            file_content.append(content)
            json.dump(file_content, file)

    def close(self):
        self.file.close()
