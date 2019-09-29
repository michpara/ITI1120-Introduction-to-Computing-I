#Exercise 1
def ah(l, x, y):
    '''(list, integer, integer) -> (tuple)
    preconditions: x <= y
    returns the # of elements in list between x and y (inclusive) and the minimum number of those'''
    betweenCount = 0
    betweenList = []
    for i in l:
        if x<= i <= y:
            betweenCount += 1
            betweenList.append(i)
    return (betweenCount, min(betweenList))

#Exercise 2
def perfect():
    '''()->(integer)
    prints all four perfect numbers less than 10000'''
    total = 0
    for i in range(1, 10000):
        for j in range(1, i):
            if i%j == 0:
                total+=j
        if(total == i):
            print(i)
        total = 0
        
#Exercise 3        
def is_perfect(num):
    '''(integer) -> (boolean)
    preconditions: num is positive
    returns true if num is perfect'''
    total = 0
    for i in range(1, num):
        if(num%i ==0):
            total += i
    return total == num

#Exercise 3a
def arithmetic(nums):
    '''(list)-> (boolean)
    returns true if the difference between every pair of consecutive numbers is the same'''
    if len(nums) == 1:
        return True

    diff = nums[1] - nums[0]
    for i in range(len(nums)-1):
        if(nums[i+1] - nums[i] != diff):
            return False
    return True

#Exercise 3b
def is_sorted(nums):
    '''(list) -> (boolean)
    returns true if nums is ordered from smallest to largest'''
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True
