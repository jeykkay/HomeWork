from file_worker import FileWorker


def app():
    fw = FileWorker('qwe.json')
    content = fw.read()
    print(content)

    fw.append('obj1')
    fw.append('obj2')
    fw.close()


app()
