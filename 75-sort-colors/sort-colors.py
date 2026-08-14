class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)-1):
            min=i
            for j in range(i,len(nums)):
                if nums[j]<=nums[min]:
                    min=j
            temp=nums[i]
            nums[i]=nums[min]
            nums[min]=temp
        return nums
        