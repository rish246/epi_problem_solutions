import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    unique_elements_idx, cur_unique_element = 0, None
    for cur_idx, cur_element in enumerate(A):
        if cur_element != cur_unique_element:
            A[unique_elements_idx] = cur_element
            cur_unique_element = cur_element
            unique_elements_idx += 1
    return unique_elements_idx


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
