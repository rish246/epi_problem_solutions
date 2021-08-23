from typing import List

from test_framework import generic_test
import random

# time -> O(n)
# space -> O(1)
def min_dist_fast(A: List[int]) -> int:
	furthest_reach_so_far, final_index = 0, len(A) - 1
	i = 0
	min_jumps = 0
	while i <= furthest_reach_so_far and furthest_reach_so_far < final_index:
		new_reach = i + A[i]
		if new_reach > furthest_reach_so_far:
			furthest_reach_so_far = new_reach
			min_jumps += 1
		i += 1

	return min_jumps


# time -> O(n ** 2)
# space -> O(n)
def min_dist_naive(A: List[int]) -> int:
	dist_to_reach = [999999999] * len(A)
	dist_to_reach[0] = 0
	for i in range(len(A)):
		cur_jump = min(i + A[i] + 1, len(A))
		for j in range(i, cur_jump):
			dist_to_reach[j] = min(dist_to_reach[j], dist_to_reach[i] + 1) # write something here
	return dist_to_reach[-1]

def can_reach_end(A: List[int]) -> bool:
	furthest_reach_so_far, final_index = 0, len(A) - 1
	i = 0
	while i <= furthest_reach_so_far and furthest_reach_so_far < final_index:
		furthest_reach_so_far = max(furthest_reach_so_far, i + A[i])
		i += 1
	return furthest_reach_so_far >= final_index

if __name__ == '__main__':
    #exit(generic_test.generic_test_main('advance_by_offsets.py', 'advance_by_offsets.tsv', can_reach_end))
	# check if min_dist_naive is correct
	# generate a random length
	n_cases = 100
	# generate a random arr of length
	for _ in range(n_cases):
		arr_len = random.randint(1, 10000)
		arr = [random.randint(0, 45321212) for _ in range(arr_len)]
		naive_ans = min_dist_naive(arr)
		fast_ans = min_dist_fast(arr)
		print(naive_ans == fast_ans)
	# stress fast with slow
