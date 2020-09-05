import chess

class Board:
	def __init__(self):
		self.board = chess.Board()
		
	def moves(self):
		return list(self.board.legal_moves)

	def board_values(self):
		return (self.board.board_fen(), self.board.turn, self.board.castling_rights, self.board.ep_square)

board = Board()
print(board.board_values())

