def inner_product(listA, listB):
    '''(list, list)->(integer)
    returns the inner product of listA and listB'''
    sum = 0
    for i in range(0, len(listA)):
        product = listA[i]*listB[i]
        sum+= product
    return sum
