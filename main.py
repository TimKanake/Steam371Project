import json
import time


start_time = time.time()


def pass_json_data(file):
	data = []
	with open('games.json') as f:
		for line in f:
			data.append(json.loads(line))
	return data

