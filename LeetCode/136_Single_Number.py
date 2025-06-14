from collections import Counter

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
       res=0  #n^0=n
       for n in nums:
           res = n ^ res
       return res
    
solution_instance = Solution()
nb = [2, 2,1,1,3]
print(solution_instance.singleNumber(nb))