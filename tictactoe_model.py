import numpy


class TicTacToeModel:
	def __init__(self):
		self.grid = numpy.zeros(shape=(3,3))
		self.turn = 1

	def update_grid(self, row, col):
		self.grid[row, col] = 1 if self.turn == 1 else -1
		self.turn = 2 if self.turn == 1 else 1