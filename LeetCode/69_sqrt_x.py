import math

x = int(input("hmm"))


class Solution:
    def mySqrt(self,x:int)->int:
        return int(math.sqrt(x))
    

s1=Solution()
print(s1.mySqrt(x))