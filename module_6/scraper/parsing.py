import requests
from lxml import html
 
def get_info():
    r = requests.get("https://auto.ru/moskva/cars/used/")
    tree = html.fromstring(r.content)

    titles = tree.xpath(
        '//a[@class="Link ListingItemTitle__link"]//text()'
    )

    prices = [
        price.replace(u'\xa0', ' ') 
        for price in tree.xpath(
            '//div[@class="ListingItemPrice-module__content"]//text()')
    ]
    
    params = [
        param.replace(u'\xa0', ' ').replace(u'\u2009', ' ')
        for param in tree.xpath(
            '//div[@class="ListingItemTechSummaryDesktop__cell"][1]//text()')
    ][::2]
    
    print(params)

if __name__ == '__main__':
    get_info()