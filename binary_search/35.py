class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, h, m = 0, len(nums) - 1, 0
        while l <= h:
            m = ((h - l) // 2) + l
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                h = m - 1

        if nums[m - 1] < target < nums[m]:
            return m
        elif target > nums[m]:
            return m + 1
        else:
            return max(0, m - 1)
