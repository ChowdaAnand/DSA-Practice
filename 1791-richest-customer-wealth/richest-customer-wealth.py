class Solution(object):
    def maximumWealth(self, accounts):
        maxsum=0
        for i in range(len(accounts)):
            total=0
            for j in range(len(accounts[i])):
                total+=accounts[i][j]
            if total>maxsum:
                maxsum=total
        return maxsum
        
        