class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Moore Voting Algorithm
        major_idx, major_count = 0, 1
        for i in range(1, len(nums)):
            if major_count == 0:
                major_idx, major_count = i, 1
            elif nums[major_idx] != nums[i]:
                major_count -= 1
            else:
                major_count += 1
        return nums[major_idx]
