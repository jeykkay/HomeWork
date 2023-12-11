import json


class DataStorage:
    def __init__(self, path_to_file, status='disconnected', content=None):
        self._path_to_file = path_to_file
        self.status = status
        self.content = content
        self._file = None

    @property
    def path(self):
        return self._path_to_file

    def _create_storage(self):
        self._file = open(self._path_to_file, 'w')
        return self._file

    def connect(self):
        if self.status == 'disconnected':
            try:
                self._file = open(self._path_to_file, 'r')
                self.content = self._file.read()
                self.status = 'connected'
            except FileNotFoundError:
                self._create_storage()
        return self._file

    def disconnect(self):
        if self.status == 'connected':
            self._file.close()
            self.status = 'disconnected'
            print('File close')


class DataStorageWrite(DataStorage):
    def connect(self):
        if self.status == 'disconnected':
            try:
                self._file = open(self._path_to_file, 'a')
                self.status = 'connected'
            except FileNotFoundError:
                self._create_storage()
        return self._file

    def _create_storage(self):
        return open(self._path_to_file, 'a')

    def append(self, _content):
        with self.content() as file:
            json.dump(_content, file)
            self.disconnect()
