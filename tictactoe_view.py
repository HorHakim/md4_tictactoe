from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import uic

import os

class TicTacToeView(QMainWindow):
	def __init__(self):
		super(TicTacToeView, self).__init__()
		uic.loadUi(os.path.join(os.path.split(__file__)[0], "tictactoe.ui"), self)
		self.symbols = {f"player_{i}" : QIcon(QPixmap(f"./player_{i}.png")) for i in [1, 2]}
		self.show()



	def check_cell(self, row, col, current_turn):
		self.findChild(QPushButton, f"pb_{row}_{col}").setIcon(self.symbols[f"player_{current_turn}"])
		self.findChild(QPushButton, f"pb_{row}_{col}").setEnabled(False)