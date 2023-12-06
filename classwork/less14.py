class MyHashMap:
    def __init__(self):
        self.map = []

    def put(self, key, value):
        for i in self.map:
            if i[0] == key in self.map:
                i[1] = value
                return
        self.map.append([key, value])

    def get(self, key):
        for i in self.map:
            if i[0] == key:
                return i[1]
        return -1

    def remove(self, key):
        for i, value in enumerate(self.map):
            if value[0] == key:
                self.map.pop(i)


hm = MyHashMap()
hm.put(1, 34)
hm.put(2, 34)
hm.put(32, 2)
print(hm.map)
print(hm.get(2))
