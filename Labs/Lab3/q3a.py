def is_divisible(n, m):
    '''(integer, integer) -> (boolean)
    returns if n is divisible by m'''
    return n%m == 0

x = int(input("Enter 1st integer: "))
y = int(input("Enter 2nd integer: "))
if(is_divisible(x,y)):
    answer = 'divisible'
else:
    answer = 'not divisible'
print(f'{x} is {answer} by {3}')
