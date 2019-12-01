import requests
import re
import json
from bs4 import BeautifulSoup


cookies = {'steamLoginSecure': 'Your Cookie'}

url = 'https://steamcommunity.com/profiles/76561198158487803/games/?tab=all'
soup = BeautifulSoup(requests.get(url, cookies=cookies).text, "lxml")
print(soup)

'''
{"appid": 578080, "name": "PLAYERUNKNOWN'S BATTLEGROUNDS",
 "logo": "https:\/\/steamcdn-a.akamaihd.net\/steam\/apps\/578080\/capsule_184x69.jpg", "friendlyURL": 578080,
 "availStatLinks": {"achievements": true, "global_achievements": true, "stats": false, "gcpd": false,
                    "leaderboards": false, "global_leaderboards": false}, "hours_forever": "338",
 "last_played": 1573638854}
'''

'''
{"appid": 251570, "name": "7 Days to Die",
 "logo": "https:\/\/steamcdn-a.akamaihd.net\/steam\/apps\/251570\/capsule_184x69.jpg", "friendlyURL": 251570,
 "availStatLinks": {"achievements": true, "global_achievements": true, "stats": false, "gcpd": false,
                    "leaderboards": false, "global_leaderboards": false}}
'''

