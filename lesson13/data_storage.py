class DataStorage:
    def __init__(self, path_to_file):
        self.__path = path_to_file
        self.status = 'disconnect'
        self.content = None
        self.file = None

    @property
    def path(self):
        return self.__path

    def _create_storage(self):
        self.file = open(self.path, 'w')
        return self.file

    def connect(self):
        try:
            self.file = open(self.path, 'r')
            self.status = 'connect'
            self.content = self.file.read()
            return self.file
        except FileNotFoundError:
            self._create_storage()
            self.status = 'connect'
            return self.file

    def disconnect(self):
        self.file.close()
        print('File closed')


class DataStorageWrite(DataStorage):
    def connect(self):
        super().connect()
        self.disconnect()
        self.file = open(self.path, 'a+')

    def _create_storage(self):
        super()._create_storage()

    def append(self, _content):
        self.file.write(_content)


dsw = DataStorageWrite('my.json')
dsw.connect()
print(dsw.content)
dsw.append('some text')
dsw.disconnect()
dsw.connect()
