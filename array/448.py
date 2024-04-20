class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        return list(set([i for i in range(1, len(nums) + 1)]).difference(set(nums)))
