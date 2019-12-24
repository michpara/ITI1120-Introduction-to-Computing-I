def first_one(L):
    '''(list)->(integer)
    preconditions: L is a list of 0's and 1's where all 0's come before 1's
    returns the position of the first 1 in L'''
    start = 0
    end = len(L)-1

    while end >= start:
        mid = (start+end)//2

        if len(L) == 2:
            if L[0] == 1:
                return 0
            elif L[1] == 1:
                return 1
            return -1

        elif(L[mid] == 0):
            start = mid + 1

        else:
            if L.index(L[mid]) == 0:
                return 0
            elif(L[mid-1] == 1):
                end = mid -1
            else:
                return mid
    return -1
