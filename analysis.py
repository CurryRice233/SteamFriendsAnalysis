import pickle
import collections
import matplotlib.pyplot as plt


class Game(object):
    def __init__(self, name, players, hours, max_player, max_hours):
        self.name = name
        self.players = players
        self.hours = hours
        self.max_player = max_player
        self.max_hours = max_hours


friends = pickle.load(open("./data.txt", 'rb'))

games = {}
no_data_players = 0

for friend in friends:
    if friend.games is not None and len(friend.games) > 0 and "hours_forever" in friend.games[0]:
        game_name = friend.games[0]['name']
        hours = float(friend.games[0]['hours_forever'].replace(',', ''))
        if friend.games[0]['name'] in games:
            games[game_name].players += 1
            games[game_name].hours += hours
            if games[game_name].max_hours < hours:
                games[game_name].max_hours = hours
                games[game_name].max_player = friend.name
        else:
            games[game_name] = Game(game_name, 1, hours, friend.name, hours)

    else:
        no_data_players += 1

print("Player no data: " + str(no_data_players))
sorted_games = collections.OrderedDict(sorted(games.items(), key=lambda x: x[1].hours, reverse=True))

game_name = []
game_hours = []
game_max = []

for game in sorted_games:
    game_name.append(games[game].name)
    game_hours.append(games[game].hours)
    game_max.append(games[game].max_hours)
    print("\nGame Name: " + games[game].name + "\n"+str(games[game].players)+" player with " + str(games[game].hours) + "h\nMax Player: " +
          str(games[game].max_player) + " was played " + str(games[game].max_hours) + "h")

plt.subplots_adjust(left=0.2)
plt.barh(range(len(game_name)), game_hours, label='Total Hours')
plt.barh(range(len(game_name)), game_max, label='Max Played', tick_label=game_name)
plt.gca().invert_yaxis()
for i, v in enumerate(game_hours):
    plt.text(v, i + .25, str(v))

for i, v in enumerate(game_max):
    plt.text(v, i + .25, str(v))

plt.legend()
plt.show()
