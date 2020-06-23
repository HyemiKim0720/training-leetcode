# 409. Longest Palindrome
#
#
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic={}
        result =0
        odd=0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=s.count(s[i])
        for j in dic.values():
            if j%2==1:
                odd=1
                result = result+j-1
            if j%2==0 and j!=0:
                result = result+j
        if odd==1:
            result=result+1
        return result
