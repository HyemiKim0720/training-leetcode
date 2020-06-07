# 7. Reverse Integer
#
#
import math
class Solution:
    def reverse(self, x: int) -> int:
        temp=x
        result=''
        if x<0: 
            temp *= (-1)
        result = str(temp)[::-1]
        if int(result)> 2147483647: 
            return 0
        if x<0: 
            result = '-'+result
        return int(result)