class BaseHandler:
    def __init__(self, path):
        self._path = path
        self.file = None

    @property
    def path(self):
        return self._path

    def read(self):
        raise NotImplementedError

    def append(self, content):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError
