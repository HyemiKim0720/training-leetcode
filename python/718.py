# 718. Maximum Length of Repeated Subarray
#
#
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp=[[0 for i in B] for j in A]
        result=0
        
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]==B[j]:
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i-1][j-1]+1
                if dp[i][j]>result:
                    result=dp[i][j]
        return result
