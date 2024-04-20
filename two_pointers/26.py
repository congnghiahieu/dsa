class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        next_idx = 0

        for n in nums:
            if next_idx < 1 or n != nums[next_idx - 1]:
                nums[next_idx] = n
                next_idx += 1

        return next_idx
