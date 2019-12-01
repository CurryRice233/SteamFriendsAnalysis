import requests
import re
import json
from bs4 import BeautifulSoup
from player import Player


def get_games(profile_link):
    bs = BeautifulSoup(requests.get(profile_link).text, "lxml")
    pattern = re.compile(r"var rgGames = (.*);")
    script = bs.find('script', text=pattern)
    match = pattern.search(script.text)
    return json.loads(match.group(1))


url = 'https://steamcommunity.com/profiles/76561198158810211/friends/'  # 需要爬数据的网址
page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml")
names = soup.find_all('div', class_='friend_block_content')
profiles = soup.find_all('a', class_='selectable_overlay')

friends = []
for i in range(len(names)):
    friends.insert(i, Player(names[i].contents[0], profiles[i].get('href'), get_games(profiles[i].get('href'))))

for friend in friends:
    print("\nname: " + friend.name + "\tlink: " + friend.link)
