def has_33(nums):
    
    for i in range(len(nums)-1):
        
        if nums[i:i+2] == [3,3]:
            return True
        
    return False

l= [int(i) for i in input().split()]


if has_33(l)==True:
    
    print("True")
    
else:
    print("False")
