class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        min_diff = 999_999
        for i in range(k - 1, len(nums)):
            min_diff = min(min_diff, nums[i] - nums[i - k + 1])
        return min_diff
