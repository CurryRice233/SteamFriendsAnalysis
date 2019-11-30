import requests
from lxml import etree
url = 'https://steamcommunity.com/profiles/76561198158810211/friends/'  # 需要爬数据的网址
page = requests.get(url)
html = etree.HTML(page.text)
result = html.xpath('//*')
print(result)