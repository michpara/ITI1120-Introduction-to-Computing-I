def m(i):
    '''(integer)->float
    returns the following series m(i) = 1/3 + 2/5 + 3/7 + i/(2i+1)'''
    if i == 1:
        return 1/3
    return m(i-1) + i/((i*2)+1)


