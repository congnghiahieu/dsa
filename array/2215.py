class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        return [
            [n for n in set_1 if n not in set_2],
            [n for n in set_2 if n not in set_1],
        ]
