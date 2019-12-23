def sum_odd_while_v2(n):
    '''(integer) -> (integer)
    computes the sum of all integers between 5 and n inclusively'''
    sum = 0
    for i in range(5, n+1, 2):
        sum += i
    return sum

