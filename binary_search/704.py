class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = ((h - l) // 2) + l
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                h = mid - 1
            else:
                return mid
        return -1
