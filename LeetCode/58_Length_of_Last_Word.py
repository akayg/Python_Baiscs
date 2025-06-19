class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        rs = s[::-1]
        word = rs.split()
        fword = word[0]
        return len(fword)
    

s1= Solution()
print(s1.lengthOfLastWord("Hlo World"))