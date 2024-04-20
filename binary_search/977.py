class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        i, j, k, ans = 0, len(nums) - 1, len(nums) - 1, [0] * len(nums)

        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                ans[k] = nums[j] ** 2
                k, j = k - 1, j - 1
            else:
                ans[k] = nums[i] ** 2
                k, i = k - 1, i + 1

        return ans
