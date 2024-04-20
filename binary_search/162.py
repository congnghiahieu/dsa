class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        return self._findPeakElement(nums, 0, len(nums) - 1)

    def _findPeakElement(self, nums: list[int], l: int, h: int):
        # 1 <= nums.length <= 1000
        # -231 <= nums[i] <= 231 - 1
        # nums[i] != nums[i + 1] for all valid i.

        if l >= h:  # This case is l == h
            if self._isPeak(nums, l):
                return l
            if self._isPeak(nums, h):
                return h
            return -1

        m = ((h - l) // 2) + l
        if self._isPeak(nums, m):
            return m

        return max(
            self._findPeakElement(nums, l, m - 1),
            self._findPeakElement(nums, m + 1, h),
        )

    def _isPeak(self, nums: list[int], idx: int):
        return (
            True
            if (idx == 0 or nums[idx] > nums[idx - 1])
            and (idx == len(nums) - 1 or nums[idx] > nums[idx + 1])
            else False
        )
