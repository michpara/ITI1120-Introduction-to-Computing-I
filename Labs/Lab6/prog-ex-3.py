def first_neg(nums):
    '''(list)->(integer)
    returns the first index of a negative number'''
    if len(nums) == 0:
        return None
    for i in nums:
        if i < 0:
            return nums.index(i)
        
