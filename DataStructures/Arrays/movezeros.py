class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        i=0
        while(i<len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                count+=1
            else:
                i+=1
        l=nums.extend(count*[0])

        return(l)
        
obj = Solution()
print(obj.moveZeroes([0,0,1,0,3,0,12]))