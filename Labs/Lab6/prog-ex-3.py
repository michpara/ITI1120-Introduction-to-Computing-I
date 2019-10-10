def first_neg(nums):
    for i in nums:
        if i < 0:
            return nums.index(i)
        
