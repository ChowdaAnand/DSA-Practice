class Solution(object):
    def sortArray(self, nums):
        low=0
        high=len(nums)-1
        def mergesort(nums,low,high):
            if low>=high:
                return 
            mid=(low+high)//2
            mergesort(nums,low,mid)
            mergesort(nums,mid+1,high)
            merge(nums,low,mid,high)
        def merge(nums,low,mid,high):
            temp=[]
            left=low
            right=mid+1
            while(left<=mid and right<=high):
                if nums[left]<=nums[right]:
                    temp.append(nums[left])
                    left+=1
                else:
                    temp.append(nums[right])
                    right+=1
            while(left<=mid):
                temp.append(nums[left])
                left+=1
            while(right<=high):
                temp.append(nums[right])
                right+=1
            for i in range(len(temp)):
                nums[low+i]=temp[i]
        mergesort(nums,low,high)
        return nums


        