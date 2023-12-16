from base_handler import BaseHandler


class TxtHandler(BaseHandler):
    def read(self):
        self.file = open(self._path, 'r')
        data = self.file.read()
        return data

    def append(self, content):
        file = open(self._path, 'a+')
        file.write(content)
        return self.file

    def close(self):
        self.file.close()
