class Solution:
    def climbStairs(self, n: int) -> int:
        if n%2==0:
            for np in range(0,int(n/2)):
                print("+2 Steps")
        else :
            print("1 Step +")
            for np in range(0,int(n/2)):
                print("+2 Steps")


s1=Solution()
s1.climbStairs(7)
