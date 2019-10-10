def sum_5_consecutive_f(nums):
    for i in range(0, len(nums)-4):
        if((nums[i] + nums[i+1] + nums[i+2] + nums[i+3] + nums[i+4]) == 0):
            return True
    return False

def sum_5_consecutive_w(nums):
    i=0
    while(i<len(nums)-4):
        if((nums[i] + nums[i+1] + nums[i+2] + nums[i+3] + nums[i+4]) == 0):
            return True
        i+=1
    return False


            
