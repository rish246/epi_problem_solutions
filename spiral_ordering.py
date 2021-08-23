from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
	len_mat = len(square_matrix)
	n_rows, n_cols = len_mat, len_mat

	def traverse_clockwise(row, col):
		nonlocal n_rows, n_cols
		clockwise_traversal = []
		# right --> DONE
		i, j = row, col		
		for j in range(col, n_cols-col):
			clockwise_traversal.append(square_matrix[i][j])
		# bottom --> DONE
		for i in range(row+1, n_rows-row):
			clockwise_traversal.append(square_matrix[i][j])
		# left --> DONE
		for j in range(j-1, col-1, -1):
			clockwise_traversal.append(square_matrix[i][j]) 
		# top --> DONE
		for i in range(i-1, row, -1):
			clockwise_traversal.append(square_matrix[i][j])
		return clockwise_traversal

	cur_row, cur_col = 0, 0
	spiral_order = []
	while cur_row in range(len_mat // 2 + 1): # (1) -> Now it won't run anyMore
		spiral_order += traverse_clockwise(cur_row, cur_col)
		cur_row += 1
		cur_col += 1
	return spiral_order


	

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
