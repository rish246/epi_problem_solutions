from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    # TODO - you fill in here.
    #return None
	if L1 is None:
		return L2

	if L2 is None:
		return L1

	# Merge
	final_list = None 
	if L1.data < L2.data:
		# new head is L1 
		#pass
		L1.next = merge_two_sorted_lists(L1.next, L2)
		final_list = L1
	else:
		# new head is L2
		L2.next = merge_two_sorted_lists(L1, L2.next)
		final_list = L2

	return final_list



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
