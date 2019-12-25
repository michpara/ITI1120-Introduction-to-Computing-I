def count_digits(n):
    '''(integer)->integer
    counts the number of digits in a given positive integer n'''
    if n//10 == 0:
        return 1
    return count_digits(n//10) + 1
