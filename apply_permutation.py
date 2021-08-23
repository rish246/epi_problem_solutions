from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
	# Look for a faster solution... this is slow for the interview
    for i, elem in enumerate(A):
    	cur_idx = i
    	while perm[i] != i:
    		cur_idx = perm[cur_idx]
    		A[cur_idx], A[i] = A[i], A[cur_idx]
    		perm[cur_idx], perm[i] = perm[i], perm[cur_idx]



def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
