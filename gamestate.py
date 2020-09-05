import chess
import chess.pgn


class Board:
	def __init__(self):
		self.board = chess.Board()
		print(self.board.legal_moves)
		print(self.board)


board = Board()

