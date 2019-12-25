def gcd(a, b):
    '''(integer, integer)->integer
    preconditions: a>=b
    finds the greatest common divisor of a and b'''
    if(b == 0):
        return a
    return gcd(b, a%b)
