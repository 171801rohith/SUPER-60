from lxml import html
import requests

response = requests.get("https://www.geeksforgeeks.org/python/python-web-scraping-tutorial/")
tree = html.fromstring(response.content)

link_titles = tree.xpath('//a/text()')

for title in link_titles:
    print(title)