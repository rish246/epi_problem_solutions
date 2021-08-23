from typing import List
import random
from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
	products = []
	sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
	num1[0], num2[0] = abs(num1[0]), abs(num2[0])

	# products not being computed properly
#	print(num1, num2)
	for i, n1 in enumerate(reversed(num2)):
		cur_prod = ['0'] * i
#		print(cur_prod)
		carry = 0
		for j, n2 in enumerate(reversed(num1)):
			sum_n = n1 * n2 + carry
			new_term = sum_n % 10
			carry = sum_n // 10
			cur_prod.append(str(new_term))
		cur_prod.append(str(carry))
#		print(n1, n2, cur_prod)
		products.append(cur_prod[::-1])

	# this is wrong... anyways
	int_prods = [int(''.join(prod)) for prod in products]
	sum_vals = sum(int_prods)
#	print(products)
	sum_arr = [int(digit) for digit in list(str(sum_vals))]
	sum_arr[0] *= sign
	return sum_arr

def my_own_test():
	def parse_int(n):
		n_list = list(str(n))
		sign = 1
		start_idx = 0
		if n_list[0] == '-':
			start_idx = 1
			sign = -1
		n_list = [int(n_list[i]) for i in range(start_idx, len(n_list))]
		n_list[0] *= sign
		return n_list

	def print_case(num1, num2, ans):
		print('---------------')
		print(ans)
		print('---------------')
		print(multiply(parse_int(num1), parse_int(num2)))			
		print('')
	

	n_cases = 100		
	lower_limit = -788779897898978
	upper_limit = 8878655678887656
	for _ in range(n_cases):
		num1 = random.randint(lower_limit, upper_limit)
		num2 = random.randint(lower_limit, upper_limit)
		ans = parse_int(num1 * num2)
		did_tc_pass = multiply(parse_int(num1), parse_int(num2)) == ans
		print(did_tc_pass)
		if not did_tc_pass:
			print_case(num1, num2, ans)
		
	
		

if __name__ == '__main__':
	exit(generic_test.generic_test_main('int_as_array_multiply.py', 'int_as_array_multiply.tsv', multiply))
#	testn1 = [-1, 7]
#	testn2 = [2, 1, 3]
#	print(multiply(testn1, testn2))
#	my_own_test()
