import copy
from portfolio_site.sudoku.sudoku_constants import SUDOKUS, NAMES, LOCATIONS, GRIDFINDER

class Sudoku:
	def __init__(self, difficulty="Easy #1"):
		self.grid = SUDOKUS.get(difficulty)
		self.difficulty = difficulty
		self._rows = {}
		for i in range(0,9):
			self._rows[i] = self.grid[i]

	def __repr__(self):
		return f"{self.grid}"

	def load_new(self, difficulty):
		self.grid = SUDOKUS[difficulty]
		self.difficulty = difficulty

	def reset(self):
		self.grid = SUDOKUS[self.difficulty]

	def generate(self):
		for row in self.grid:
			print(row)

	def solve(self):
		self._recursive_solver()
		self.grid = saved_grid
	
	def _recursive_solver(self):
		for x in range(1,10):
			for y in range(1,10):
				if self.grid[x-1][y-1] == 0:
					for i in range(1,10):
						if self._valid_spot(i,x,y):
							self.grid[x-1][y-1] = i
							self._recursive_solver()
							self.grid[x-1][y-1] = 0
					return
				else:
					pass
		global saved_grid
		saved_grid = copy.deepcopy(self.grid)	

	def _valid_spot(self, guess, row, col):

		def _row_check():
			if guess in self.grid[row-1]:
				return False
			else:
				return True

		def _col_check():
			for j in range(0,9):
				if guess == self.grid[j][col-1]:
					return False
				else:
					pass
			return True

		def _grid_check():
			def _inner_check(grid_num):
				section_bot_and_top = GRIDFINDER[grid_num]
				section_bot, section_top, bot, top = section_bot_and_top
				for i in range(section_bot, section_top):
						if guess in self.grid[i][bot:top]:
							return False
						else:
							pass
				return True

			if row <= 3:
				if col <= 3:
					if _inner_check(1):
						return True
				elif col >= 4 and col < 7:
					if _inner_check(2):
						return True
				else:
					if _inner_check(3):
						return True

			elif row >= 4 and row < 7:
				if col <= 3:
					if _inner_check(4):
						return True
				elif col >= 4 and col < 7:
					if _inner_check(5):
						return True
				else:
					if _inner_check(6):
						return True

			else:
				if col <= 3:
					if _inner_check(7):
						return True
				elif col >= 4 and col < 7:
					if _inner_check(8):
						return True
				else:
					if _inner_check(9):
						return True

		if _row_check():
			if _col_check():
		 		if _grid_check():
		 			return True
		else:
			pass

if __name__ == "__main__":
	print("Original Sudoku:")
	sudoku = Sudoku()
	sudoku.generate()
	print("Solved Sudoku:")
	sudoku.solve()
	sudoku.generate()
	print("Load New Sudoku:")
	sudoku.load_new("Easy #3")
	sudoku.generate()
	print("Reset Sudoku:")
	sudoku.reset()
	sudoku.generate()
