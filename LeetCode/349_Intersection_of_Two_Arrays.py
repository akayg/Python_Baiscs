class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n1=set(nums1)
        n2=set(nums2)
        return list(n1 & n2)

s1=Solution()

print(s1.intersection([1,2,3,12,2,2,2],[2,222,1]))