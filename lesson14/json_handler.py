import json


from base_handler import BaseHandler


class JsonHandler(BaseHandler):
    def __init__(self, path):
        super().__init__(path)

    def open_file(self, mode):
        self.file = open(self._path, mode)

    def read(self):
        try:
            self.open_file('r')
            data = json.load(self.file)
            return data
        except json.decoder.JSONDecodeError:
            raise FileNotFoundError('The content must be in list format')

    def append(self, content):
        data = self.read()
        data.append(content)
        self.open_file('w')
        json.dump(data, self.file)

    def close(self):
        self.file.close()
