class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        return self._singleNonDuplicate(nums, 0, len(nums) - 1)

    def _singleNonDuplicate(self, nums: list[int], l: int, h: int):
        # 1 <= nums.length <= 105
        # 0 <= nums[i] <= 105

        if l >= h:  # This case is l == h
            return nums[l] if self._isSingle(nums, l) else -1

        m = ((h - l) // 2) + l
        if self._isSingle(nums, m):
            return nums[m]

        return max(
            self._singleNonDuplicate(nums, l, m - 1),
            self._singleNonDuplicate(nums, m + 1, h),
        )

    def _isSingle(self, nums: list[int], idx: int):
        return (
            True
            if (idx == 0 or nums[idx] != nums[idx - 1])
            and (idx == len(nums) - 1 or nums[idx] != nums[idx + 1])
            else False
        )
