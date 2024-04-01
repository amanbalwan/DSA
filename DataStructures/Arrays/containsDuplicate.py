# class Solution:
#     def containsDuplicate(self, nums):
#         while(nums is not None):
#             temp=nums[0]
#             nums.pop(0)
#             if temp in nums:
#                 return True
#         return False

# obj=Solution()
# print(obj.containsDuplicate([1,2,3,1]))
        
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False
