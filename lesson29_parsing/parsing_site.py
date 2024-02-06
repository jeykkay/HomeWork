from requests import get

from lxml import html


url = 'https://gippo-market.by/catalog/'
response = get(url)
products = []

req_links_categories = '//div[@class="price"]/text()'
dom_catalog = html.fromstring(response.text)
categories = dom_catalog.xpath(req_links_categories)

while categories:
    category = categories.pop()
    response = get(f'{url}{category}')

    req_under_category = '//div[@class="link-arrow link-arrow--green"]/a/@ref'
    under_category_dom = html.fromstring(response.text)
    under_category = under_category_dom.xpath(req_under_category)

    if under_category:
        print(f'{category} extend {under_category}')
        categories.extend(under_category)
    else:
        print(f'Products found')
        req_products = '//a[@class="product-card__img-wrap"]/@href'
        products.extend(under_category_dom.xpath(req_products))

for prod in products:
    print(prod)

print(products)

