class Solution:
    def isValid(self, s:str) -> bool:
        cuted = list(s)
        if "(" in cuted:
            if ")" in cuted:
                return True
        elif "[" in cuted:
            if "]" in cuted:
                return True
        elif "{" in cuted:
            if "}" in cuted:
                return True
        return False
    
s1 = Solution()
print(s1.isValid("yusdghf hjs []sh"))