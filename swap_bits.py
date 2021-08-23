from test_framework import generic_test

def unset_bit(num, n):
	unset_mask = ~(1 << n)
	return num & unset_mask

def set_bit(num, n):
	set_mask = 1 << n
	return num | set_mask

def change_nth_bit(num, n, new_val):
	if new_val >= 1:
		return set_bit(num, n)
	return unset_bit(num, n)


def swap_bits(x, i, j):
	return swap_bits_brute(x, i, j)

########### Make a new function named swap_bits_fast() ##################

def swap_bits_brute(x, i, j):
	i_bit_val = (1 << i) & x
	j_bit_val = (1 << j) & x
	x = change_nth_bit(x, i, j_bit_val)
	x = change_nth_bit(x, j, i_bit_val)
	return x	


if __name__ == '__main__':
    exit(
    	generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
