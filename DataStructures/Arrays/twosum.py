class Solution:
    def twoSum(self, nums, target):
        rem=[]
        for i in nums:
            if i in rem:
                return [rem.index(i),len(rem)]
            else:
                rem.append(target-i)

ob= Solution()
print(ob.twoSum([2,7,11,15],9))
                    

            

