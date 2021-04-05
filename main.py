def print_sudoku(sudoku):
	for i in sudoku:
		print(i)

def null_number(sudoku):
	"""Procura um espaço vazio e retorna
	uma tupla com sua localização"""
	for r in range(9):
		for c in range(9):
			if sudoku[r][c] == 0:
				return (r, c, True)
	return (None, None, False)

def verify_row(sudoku, num:int, row:int):
	for i in range(9):
		if sudoku[row][i] == num:
			return False
	return True

def verify_column(sudoku, num:int, column:int):
	for i in range(9):
		if sudoku[i][column] == num:
			return False
	return True

def verify_square(sudoku, num:int, row:int, column:int):
	start_row = row // 3 * 3
	start_column = column // 3 * 3
	for r in range(start_row, start_row+3):
		for c in range(start_column, start_column+3):
			if sudoku[r][c] == num:
				return False
	return True

def verify_table(sudoku, num:int, row:int, column:int):
	if verify_row(sudoku, num, row) and verify_column(sudoku, num, column) and verify_square(sudoku, num, row, column):
		return True
	return False

def solve_sudoku(sudoku):
	row = null_number(sudoku)[0]
	column = null_number(sudoku)[1]
	is_something_null = null_number(sudoku)[2]

	if is_something_null:
		for i in range(1, 10):
			if verify_table(sudoku, i, row, column):
				sudoku[row][column] = i

				if solve_sudoku(sudoku):
					return True
			
		sudoku[row][column] = 0
		return False
	else:
		return sudoku
		

if __name__ == "__main__":
	sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
 ]

	if solve_sudoku(sudoku):
		print_sudoku(solve_sudoku(sudoku))
	else:
		print("Sem solução")