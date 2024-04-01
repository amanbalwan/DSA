class Solution:
    def rotate(self, nums,k):
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        k%=l
        nums[:] = nums[l-k:]+nums[:l-k]
        return nums

obj = Solution()
print(obj.rotate([1,2,3,4,5,6,7],3))
