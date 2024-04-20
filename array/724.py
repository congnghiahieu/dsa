class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left, right = 0, sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            if i - 1 >= 0:
                left += nums[i - 1]
            if left == right:
                return i
        return -1
