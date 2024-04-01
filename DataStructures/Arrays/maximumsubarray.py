class Solution:
    def maxSubArray(self, nums):
        i=1
        while(i<len(nums)):
            if nums[i-1]>0:
                nums[i]+=nums[i-1]
            i+=1
        return max(nums)

obj= Solution()
print(obj.maxSubArray([1,32,4,-1,2,-4,5,6,1,-32]))