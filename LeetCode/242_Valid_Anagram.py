from collections import Counter
s = "anagram"
t = "nagaram"



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_in_s=Counter(s)
        char_in_t=Counter(t)
        if char_in_s == char_in_t:
            return True
        else : return False


s1 = Solution()
s1.isAnagram(s,t)

