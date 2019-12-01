import requests
import re
import json
from bs4 import BeautifulSoup

url = 'https://steamcommunity.com/profiles/76561198158810211/games/?tab=all'  # 需要爬数据的网址
soup = BeautifulSoup(requests.get(url).text, "lxml")

pattern = re.compile(r"var rgGames = (.*);")
script = soup.find('script', text=pattern)
match = pattern.search(script.text)
games = json.loads(match.group(1))
print(games[0]['appid'])
