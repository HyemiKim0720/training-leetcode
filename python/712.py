# 712. Minimum ASCII Delete Sum for Two Strings
#
#
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0 for j in range(len(s2))] for i in range(len(s1))]
        mstring=0
        
        for i in range(len(s1)):
            if s1[i]==s2[0]:
                dp[i][0]=ord(s1[i])
            else:
                dp[i][0]=dp[i-1][0]
                
        for i in range(len(s2)):
            if s2[i]==s1[0]:
                dp[0][i]=ord(s2[i])
            else:
                dp[0][i]=dp[0][i-1]
        
        for i in range(1,len(s1)):
            for j in range(1,len(s2)):
                if s1[i]==s2[j]:
                    dp[i][j]=dp[i-1][j-1]+ord(s1[i])
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
        s1val,s2val=0,0
        
        for i in range(len(s1)):
            s1val=s1val+ord(s1[i])
        for i in range(len(s2)):
            s2val=s2val+ord(s2[i])
        
        return s1val+s2val-(2*dp[len(s1)-1][len(s2)-1])
