class Solution(object):
    def runningSum(self, nums):
        temp=0
        for i in range(len(nums)):
            temp+=nums[i]
            nums[i]=temp
        return nums

