from file_worker import FileWorker


def app():
    fw = FileWorker('qwe.txt')
    fw.append('obj1')
    fw.append('obj2')
    print(fw.read())
    fw.close()


app()
