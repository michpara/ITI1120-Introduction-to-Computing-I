def is_divisible(n, m):
    '''(integer, integer) -> (boolean)
    returns if n is divisible by m'''
    return n%m == 0

def is_divisible23n8(x):
    '''(integer) -> (string)
    returns 'yes' if x is divisible by 2 or 3 but not by 8, 'no' otherwise'''
    if((x%2 == 0 or x%3 == 0) and x%8 != 0):
	return 'yes'
    return 'no'

x = int(input("Enter an integer: "))
if(is_divisible23n8(x) == 'yes'):
	print(f'{x} is divisible by 2 or 3 but not 8')
else:
	print(f'It is not true that {x} is divisible by 2 or 3 but not 8')
