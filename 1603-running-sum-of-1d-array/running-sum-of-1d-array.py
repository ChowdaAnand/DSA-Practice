class Solution(object):
    def runningSum(self, nums):
        sum=0
        l=[]
        for i in range(len(nums)):
            sum+=nums[i]
            l.append(sum)
        return l

        