import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r"[^a-zA-Z0-9]", '', s).lower()
        return cleaned == cleaned[::-1]

s1 = Solution()
print(s1.isPalindrome("Appa appA"))  # ✅ True



s2=Solution()
print(s2.isPalindrome("A man, a plan, a canal: Panama"))#test case by leetcode