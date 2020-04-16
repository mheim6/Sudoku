#Monica Heim


import fileinput
import time

def print_sudoku(s):
#			Formats the Sudoku puzzle currently in a 2D list into
#			a grid with lines separating the blocks for readability

	for row in range(9):
		for col in range(9):
			print(s[row][col], end=' ')
			if col+1 == 3 or col+1 == 6:
				print(" | ", end=' ')
		if row+1 == 3 or row+1 == 6:
			print("\n" + "-"*25, end=' ')
		print()
	print()

def test_cell(s, row, col):
#			Sudoku puzzle s, row, and column number, return a list which represents
#			the valid numbers that can go in that cell. 0 = possible, 1 = not possible

	used = [0]*10
	used[0] = 1
	block_row = row // 3
	block_col = col // 3

	# Row and Column
	for m in range(9):
		used[s[m][col]] = 1;
		used[s[row][m]] = 1;

	# Square
	for m in range(3):
		for n in range(3):
			used[s[m + block_row*3][n + block_col*3]] = 1

	return used

def first_try(s):
#			a Sudoku puzzle, try to solve the puzzle by iterating through each
#			cell and determining the possible numbers in that cell. If only one possible
#			number exists, fill it in and continue on until the puzzle is stuck.
	stuck = False

	while not stuck:
		stuck = True
		for row in range(9):
			for col in range(9):
				used = test_cell(s, row, col)
				if used.count(0) != 1:
					continue

				for m in range(1, 10):
					# current cell is empty and there is only one possibility then fill in the current cell
					if s[row][col] == 0 and used[m] == 0:
						s[row][col] = m
						stuck = False
						break

def algorithm_dfs(s, row, col):
#			A Sudoku puzzle ir will be solved recursively performing DFS which tries out the possible solutions and by using backtracking
	if row == 8 and col == 8:
		used = test_cell(s, row, col)
		if 0 in used:
			s[row][col] = used.index(0)
		return True

	if col == 9:
		row = row+1
		col = 0

	if s[row][col] == 0:
		used = test_cell(s, row, col)
		for i in range(1, 10):
			if used[i] == 0:
				s[row][col] = i
				if algorithm_dfs(s, row, col+1):
					return True
		# Here the puzzle has no solution
		s[row][col] = 0
		return False

	return algorithm_dfs(s, row, col+1)

def main():
	start = time.time()
	num_puzzles = 0
	s = []
	text = ""

	"""
	for s in squares:
		values = dict(s, digits)

	with open(filepath, "r") as filestream:
		with open(filepath, "w") as filestream2:
			for line in filestream:
				currentline = line.split(", ")
				#total = str(int(currentline[0]) + int(currentline[1]) + currentline[2]) + "\n"
				#filestream2.write(total)

	out = file('solution.txt', 'w')
	for line in fileinput.input():
		for num in line.strip().split(', '):
			out.write("Solution")

	for line in fileinput.input():
		currentline = line.split(", ")
		text += line
	"""

	for line in fileinput.input():
		#line = ' '.join(line.split(", "))
		currentline = line.split(", ")
		text += line

	while len(text) > 0:
		l = []

		# Get a row of numbers
		while len(l) < 9:
			if text[0].isdigit():
				l.append(int(text[0]))
			text = text[1:]

		# Insert that row into the Sudoku grid
		s.append(l)

		if len(s) == 9:
			num_puzzles += 1
			print("Puzzle Number {:d}".format(num_puzzles))
			print("Original:")
			print_sudoku(s)

			first_try(s)
			for line in s:
				if 0 in line:
					algorithm_dfs(s, 0, 0)
					break

			print("Solution:")
			print_sudoku(s)

			print("="*30)
			s = []

	print("{:.2f} seconds to solve {} puzzle(s)".format(time.time() - start, num_puzzles))

if __name__ == "__main__":
	main()
