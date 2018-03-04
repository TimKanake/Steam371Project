import json
import time
import string

printable = set(string.printable)
start_time = time.time()


def pass_json_data(file_name):
	data = []
	with open(file_name) as f:
		for line in f:
			data.append(json.loads(line))
	return data


def get_genres(genres_dict):
	genres = []
	for g in genres_dict:
		genres.append(g['description'])

	return genres


def get_platforms(platforms_dict):
	platforms = []
	for k in platforms_dict.keys():
		if platforms_dict[k]:
			platforms.append(k)

	return platforms


# Creates a Text File from a Json File.
# For this project will use another program to covert to .MELD file.
# Input: path to the json file with the game data
# Output: a games.txt file
def create_text_file(json_file_name):
	data = pass_json_data(json_file_name)
	games_data = {}
	# put all relevant game data into a dictionary with key as name of game
	for g in data:
		if g is not None:
			try:
				game = g['data']
				if game['type'] != 'game':
					continue
				game = g['data']
				game_name = game['name']
				game_genres = get_genres(game['genres'])
				try:
					game_price = game['price_overview']['initial']
				except KeyError:
					game_price = -1
				supported_platforms = get_platforms(game['platforms'])
				required_age = game['required_age']
				try:
					rating = game['metacritic']['score']
				except KeyError:
					rating = -1
				temp = [game_name, game_genres, game_price, supported_platforms, required_age, rating]
				games_data[game_name] = temp
			except KeyError:
				continue

	with open('games.txt', 'w') as f:
		for k in games_data.keys():
			# record game name
			game_name = filter(lambda x: x in printable, k.replace(" ", ""))
			f.write('(isa ' + str(game_name) + ' ComputerGameProgram)\n')
			f.write('(gameName ' + str(game_name) + ')\n')

			# record game price
			game_price = int(games_data[k][2])/100.0
			f.write('(price ' + str(game_name) + ' ' + str(game_price) + ')\n')

			# record game rating
			# game_rating = int(games_data[k][5])
			# f.write('(rating ' + str(game_name) + ' ' + str(game_rating) + ')\n')

			# record required age
			game_age = int(games_data[k][4])
			f.write('(requiredAge ' + str(game_name) + ' ' + str(game_age) + ')\n')

			# record genres
			for g in games_data[k][1]:
				f.write('(hasGenre ' + str(game_name) + ' ' + str(g.replace(" ", "")) + ')\n')

			# record supported platforms
			for g in games_data[k][3]:
				f.write('(supportsPlatform ' + str(game_name) + ' ' + str(g.replace(" ", "")) + ')\n')

	f.close()


create_text_file('games.json')
