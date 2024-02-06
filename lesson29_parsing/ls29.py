from lxml import html

with open('index.html', 'r') as f:
    read_file = html.fromstring(f.read())
    req: str = '//div[@class="items"]/a/@href'
    elems = read_file.xpath(req)

    print(elems)


