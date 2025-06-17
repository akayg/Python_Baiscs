class Solution:
    def isPalindrome(self, x: int) -> bool:
        strn_x = str(x)
        if x < 0 or ( x % 10==0 and  x != 0 ):
            return False

        return strn_x == strn_x[::-1]
        

s1=Solution()
print(s1.isPalindrome(121))