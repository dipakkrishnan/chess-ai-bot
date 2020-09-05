# Heavily influenced from geohot twitchchess


import chess.pgn
import numpy as np
import os

class Load: 
	def __init__(self):
		self.files = os.listdir("data")
		
	def load_dataset(self):
		for file in self.files:
			data = open(os.path.join("data", file))

			game = chess.pgn.read_game(data)

			print(game.headers['Result'])


loader = Load()
print(loader.load_dataset())
