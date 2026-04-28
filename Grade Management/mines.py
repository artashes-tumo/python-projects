# Terminal-based Minesweeper game
import random

class Cell:
	def __init__(self):
		self.mine = False
		self.revealed = False
		self.flagged = False
		self.adjacent = 0

class Minesweeper:
	def __init__(self, rows=9, cols=9, mines=10):
		self.rows = rows
		self.cols = cols
		self.mines = mines
		self.board = [[Cell() for _ in range(cols)] for _ in range(rows)]
		self.first_move = True
		self.flags_left = mines
		self.revealed_count = 0
		self.total_cells = rows * cols
		self.game_over = False

	def place_mines(self, safe_r, safe_c):
		positions = [(r, c) for r in range(self.rows) for c in range(self.cols) if not (r == safe_r and c == safe_c)]
		random.shuffle(positions)
		for i in range(self.mines):
			r, c = positions[i]
			self.board[r][c].mine = True
		self.calculate_adjacency()

	def calculate_adjacency(self):
		for r in range(self.rows):
			for c in range(self.cols):
				if self.board[r][c].mine:
					continue
				count = 0
				for dr in [-1, 0, 1]:
					for dc in [-1, 0, 1]:
						nr, nc = r + dr, c + dc
						if 0 <= nr < self.rows and 0 <= nc < self.cols:
							if self.board[nr][nc].mine:
								count += 1
				self.board[r][c].adjacent = count

	def print_board(self, reveal_all=False):
		print("   " + " ".join([chr(ord('A') + c) for c in range(self.cols)]))
		for r in range(self.rows):
			row_str = f"{r+1:2} "
			for c in range(self.cols):
				cell = self.board[r][c]
				if reveal_all:
					if cell.mine:
						row_str += "* "
					elif cell.adjacent > 0:
						row_str += f"{cell.adjacent} "
					else:
						row_str += ". "
				else:
					if cell.flagged:
						row_str += "F "
					elif not cell.revealed:
						row_str += "# "
					elif cell.mine:
						row_str += "* "
					elif cell.adjacent > 0:
						row_str += f"{cell.adjacent} "
					else:
						row_str += ". "
			print(row_str)
		print(f"Flags left: {self.flags_left}")

	def in_bounds(self, r, c):
		return 0 <= r < self.rows and 0 <= c < self.cols

	def reveal(self, r, c):
		cell = self.board[r][c]
		if cell.revealed or cell.flagged:
			return
		cell.revealed = True
		self.revealed_count += 1
		if cell.mine:
			self.game_over = True
			return
		if cell.adjacent == 0:
			for dr in [-1, 0, 1]:
				for dc in [-1, 0, 1]:
					nr, nc = r + dr, c + dc
					if self.in_bounds(nr, nc) and not self.board[nr][nc].revealed:
						self.reveal(nr, nc)

	def flag(self, r, c):
		cell = self.board[r][c]
		if cell.revealed:
			return
		if cell.flagged:
			cell.flagged = False
			self.flags_left += 1
		else:
			if self.flags_left > 0:
				cell.flagged = True
				self.flags_left -= 1

	def check_win(self):
		return self.revealed_count == self.total_cells - self.mines

	def play(self):
		print("Welcome to Minesweeper!\nType e.g. 'A5' to reveal, 'F B3' to flag/unflag.")
		while not self.game_over:
			self.print_board()
			move = input("Enter move: ").strip().upper()
			if move.startswith('F '):
				move = move[2:].strip()
				flag = True
			else:
				flag = False
			if len(move) < 2:
				print("Invalid input.")
				continue
			col = ord(move[0]) - ord('A')
			try:
				row = int(move[1:]) - 1
			except ValueError:
				print("Invalid row.")
				continue
			if not self.in_bounds(row, col):
				print("Out of bounds.")
				continue
			if self.first_move:
				self.place_mines(row, col)
				self.first_move = False
			if flag:
				self.flag(row, col)
			else:
				self.reveal(row, col)
				if self.game_over:
					self.print_board(reveal_all=True)
					print("BOOM! You hit a mine. Game over.")
					return
				if self.check_win():
					self.print_board(reveal_all=True)
					print("Congratulations! You cleared the minefield!")
					return

if __name__ == "__main__":
	game = Minesweeper()
	game.play()
