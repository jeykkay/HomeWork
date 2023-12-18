from base_handler import BaseHandler


class TxtHandler(BaseHandler):
    def __init__(self, path):
        self.path = path
        self.file = None

    def read(self):
        self.file = open(self.path, 'r')
        return self.file.read()

    def append(self, content):
        file = open(self.path, 'a+')
        file.write(content)

    def close(self):
        self.file.close()
