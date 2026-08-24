class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        l=""
        for i in range(len(s)-1,-1,-1):
            if s[i].isalnum():
                l+=s[i]

        return l==l[::-1]
        