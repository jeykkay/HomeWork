from json_handler import JsonHandler
from txt_handler import TxtHandler


class FileWorker:
    def __init__(self, path):
        self.path = path
        self.handler = self._file_type()

    def _file_type(self):
        if self.path.endswith('.txt'):
            return TxtHandler(self.path)
        elif self.path.endswith('.json'):
            return JsonHandler(self.path)
        else:
            raise ValueError('Incorrect file type')

    def read(self):
        return self.handler.read()

    def append(self, content):
        return self.handler.append(content)

    def close(self):
        return self.handler.close()