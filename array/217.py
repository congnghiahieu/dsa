class Solution:
    # Sort solution
    def containsDuplicate_1(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

    # Set solution
    def containsDuplicate_2(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)
