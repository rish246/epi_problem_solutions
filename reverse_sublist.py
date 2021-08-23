from typing import Optional, List

from list_node import ListNode
from test_framework import generic_test


def extract_sublist(L: ListNode, start: int, end: int) -> ListNode:
    temp = L 
    # just print the node values in given range
    cur_index = 0
    our_list = ListNode()
    our_tail = our_list 
    while temp:
        if cur_index >= start and cur_index <= end and cur_index >= 1: # 0 -> ListNode(0)
            our_tail.next = ListNode(temp.data)
            our_tail = our_tail.next 
        temp, cur_index = temp.next, cur_index + 1 

    return our_list.next

def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if L is None:
        return None
    dummy_head = ListNode()
    dummy_head.next = L 
    sublist_head = extract_sublist(dummy_head, start, finish) 
    # print(sublist_head)
    sublist_head, sublist_tail = reverse_list(sublist_head)
    # print(sublist_head)
    if sublist_head is None:
        return dummy_head.next

    head_prev, tail_next = extract_connecting_nodes(start, finish, dummy_head)
    head_prev.next, sublist_tail.next = sublist_head, tail_next
    return dummy_head.next


    return None

def extract_connecting_nodes(start, finish, dummy_head):
    cur_idx, temp = 0, dummy_head
    head_prev, tail_next = dummy_head, None
    while temp:
        if cur_idx == start - 1:
            # this is our prev_head
            head_prev = temp 

        if cur_idx == finish + 1:
            tail_next = temp

        temp, cur_idx = temp.next, cur_idx + 1
    return head_prev,tail_next


def reverse_list(L: ListNode) -> Optional[ListNode]:
    prev, cur = None, L
    # None, None
    while cur:
        next = cur.next 
        cur.next, prev, cur = prev, cur, next
    return prev, L

def list_to_llist(vals: List[int]) -> ListNode:
    dummy_head = ListNode()
    tail_node = dummy_head
    for val in vals:
        tail_node.next = ListNode(val)
        tail_node = tail_node.next
    return dummy_head.next 

def llist_to_list(root: ListNode) -> List[int]:
    result = []
    temp = root 
    while temp:
        result.append(temp.data)
        temp = temp.next 
    return result

def print_llist(root: ListNode) -> None:
    temp = root
    while temp:
        print(temp.data, sep=' ')
        temp = temp.next 



if __name__ == '__main__':
    exit(
       generic_test.generic_test_main('reverse_sublist.py',
                                      'reverse_sublist.tsv', reverse_sublist))
    # create a linked list
    test1 = [1, 2, 3], 1, 2, [2, 1, 3]
    test2 = [1], 0, 0, [1]
    test3 = [], 0, 0, []

    tests = [test1, test2, test3]
    for test_list, start, finish, ans_list in tests:
        test_llist = list_to_llist(test_list)
        our_ans_list = llist_to_list(reverse_sublist(test_llist, start, finish))
        test_pass = our_ans_list == ans_list
        if not test_pass:
            print(our_ans_list)
    # test_list1 = list_to_llist([1, 2, 3])
    # extract2 = llist_to_list(reverse_sublist(test_list1, 1, 2))
    # print(extract2 == [2, 1, 3])




    # print(extract_sublist(list_to_llist([1, 2, 3]), 1, 2))
    # extract3 = llist_to_list(reverse_sublist(test_list, 3, 8))
    # print(extract3 == [1, 3, 4, 8, 2]) # The testlist changed as well..
    # extract_null = reverse_sublist(None, 0, 0)


    # print(reverse_list(None))
