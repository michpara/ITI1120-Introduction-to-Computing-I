#5.16
def indexes(string, char):
    '''(string, string)->lst
    returns a list of indexes at with char occurs in strng'''
    lst = []
    stringList = list(string)
    for i in range(len(stringList)):
        if stringList[i] == char:
            lst.append(i)
    return lst
 
#5.17                       
def doubles(ints):
    '''(lst)->()
    prints the elements in the list that are exactly double the previous element in the list'''
    for i in range(1, len(ints)):
        if(ints[i] == ints[i-1]*2):
            print(ints[i])

#5.18
def four_letters(words):
    '''(list)->(list)
    returns the sublist of all four letter words in words'''
    lst = []
    for i in words:
        if len(i) == 4:
            lst.append(i)
    return lst

#5.19
def inBoth(lstA, lstB):
    '''(list, list)->(boolean)
    return True if there is an item common to both lstA and lstB'''
    for i in lstA:
        if i in lstB:
            return True
    return False

#5.20
def intersect(lstA, lstB):
    '''(list, list)->(list)
    preconditons: no duplicate values
    returns a list containing elements that are present in both lstA and lstB'''
    lst = []
    for i in lstA:
        if i in lstB:
            lst.append(i)
    return lst

#5.21
def pair(lstA, lstB, n):
    '''(list, list, integer)->()
    prints the pairs of inegers from lstA and lstB that add up to n'''
    for i in lstA:
        for j in lstB:
            if i + j == n:
                print(i, j)

#5.22
def pairSum(lst, n):
    '''(list, integer)->()
    preconditons: list of distinct integers
    prints the indexes of all vlaues of lst that sum to n'''
    found = []
    for i in lst:
        for j in lst:
            if i!=j and i + j == n and (i,j) not in found:
                found.append((j,i))
                print(lst.index(i), lst.index(j))

#5.29
def lastFirst(strings):
    '''(list)->()
    returns a list of first names and a list of last names'''
    first = []
    last = []
    temp = []
    for i in strings:
        temp = i.split(',')
        last.append(temp[0])
        first.append(temp[1])
    print(first, last)

#5.31
def subsetSum(lst, target):
    '''(list, integer)->(boolean)
    preconditions: lst and target hold positive values
    return True if there are three numbers in lst that add up to target'''
    for i in lst:
        for j in lst:
            for k in lst:
                if i != j != k and i+j+k == target:
                    return True
    return False

#5.33
def mystery(n):
    '''(integer)->(integer)
    preconditions: n is positive
    returns the count of times n can be halved before reaching 1'''
    count = 0
    while(n > 1):
        n = n//2
        count+= 1
    return count

#5.48
def sublist(lstA, lstB):
    '''(list, list)->(boolean)'''
    return if lstA is a sublist of lstB
    lst = []
    for i in lstB:
        if i in lstA:
            lst.append(i)
    return lstA == lst
