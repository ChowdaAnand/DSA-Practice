class Solution(object):
    def subarraySum(self, nums, k):
        mp={0:1}
        sum=0
        count=0
        for i in range(len(nums)):
            sum+=nums[i]
            reguired=sum-k
            if reguired in mp:
                count+=mp[reguired]
            if sum in mp:
                mp[sum]+=1
            else:
                mp[sum]=1
        return count
        