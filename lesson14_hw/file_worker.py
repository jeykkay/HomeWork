from json_handler import JsonHandler
from txt_handler import TxtHandler


class FileWorker:
    def __init__(self, path):
        try:
            with open(path):
                pass
        except FileNotFoundError:
            raise FileNotFoundError('File not found')
        self.path = path
        self.handler = self.get_handler()

    def get_handler(self):
        if self.path.endswith('.json'):
            return JsonHandler(self.path)
        elif self.path.endswith('.txt'):
            return TxtHandler(self.path)
        else:
            raise ValueError('Expected json or txt')

    def read(self):
        return self.handler.read

    def append(self, content):
        return self.handler.append(content)

    def close(self):
        return self.handler.close()
