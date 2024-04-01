nums = [3,4,8,11,1]
val= 13
def sum(nums,val):
    d=[]
    for i in nums:
        if val-i>0:
            if i in d:
                return True
            else:
                d.append(val-i)
    return False


print(sum(nums,val))