 import requests
from lxml import html
 def get_info():
     r = requests.get("https://auto.ru/moskva/cars/used/")
     print(r.content)
     tree = html.fromstring(r.content)

     title_xpath = tree

if __name__ == '__main__':
    get_info()