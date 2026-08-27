class Solution(object):
    def reverse(self, x):
        if x<=0:
            sign=-1
        else:
            sign=1
        rev=0
        x=abs(x)
        while(x>0):
            dig=x%10
            rev=rev*10+dig
            x=x//10
        rev=rev*sign
        if rev< -2**31 or rev>2**31-1:
            return 0
        return rev
    

       
        