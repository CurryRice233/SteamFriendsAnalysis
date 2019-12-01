import requests
import re
import json
from bs4 import BeautifulSoup
from player import Player


url = 'https://steamcommunity.com/profiles/76561198158810211/friends/'  # Your profiles
cookies = {'steamLoginSecure': 'Your Cookie'}


def get_games(profile_link):
    bs = BeautifulSoup(requests.get(profile_link, cookies=cookies).text, "lxml")
    pattern = re.compile(r"var rgGames = (.*);")
    script = bs.find('script', text=pattern)
    if script is None:
        return None
    else:
        match = pattern.search(script.text)
        return json.loads(match.group(1))


page = requests.get(url, cookies=cookies)
soup = BeautifulSoup(page.text, "lxml")
names = soup.find_all('div', class_='friend_block_content')
profiles = soup.find_all('a', class_='selectable_overlay')

friends = []
for i in range(len(names)):
    link = profiles[i].get('href')
    player = Player(names[i].contents[0], link, get_games(link + "/games/?tab=all"))
    friends.insert(i, player)
    info = "\nFriend: " + player.name
    if player.games is not None and len(player.games) > 0:
        info += "\nGame: " + player.games[0]['name']
        if "hours_forever" in player.games[0]:
            info += "\tPlayed: " + player.games[0]['hours_forever']+"h"
        else:
            info += "\tPlayed: no data"
    else:
        info += "\nNo game found!"
    print(info)

'''
for friend in friends:
    print("\nname: " + friend.name + "\tlink: " + friend.link + "\tgame: " + friend.games[0].name)
'''
