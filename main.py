import json
import time


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


def create_text_file(data):
	games_data = {}
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
					game_price = None
				supported_platforms = get_platforms(game['platforms'])
				required_age = game['required_age']
				try:
					rating = game['metacritic']['score']
				except KeyError:
					rating = None
				temp = [game_name, game_genres, game_price, supported_platforms, required_age, rating]
				games_data[game_name] = temp
			except KeyError:
				continue

	return games_data


data1 = pass_json_data('games.json')
te = create_text_file(data1)


for k in te.keys():

	print te[k], '\n\n\n'
