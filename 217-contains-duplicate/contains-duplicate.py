class Solution(object):
    def containsDuplicate(self, nums):
        count=set()
        for num in nums:
            if num in count:
                return True
            count.add(num)
        return False