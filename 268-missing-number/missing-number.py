class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        real=n*(n+1)//2
        count=0
        for i in range(n):
            count+=nums[i]
        return real-count

        