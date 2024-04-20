class Solution:
    def twoSum_1(self, nums: list[int], target: int) -> list[int]:
        # Idea: Using hash set to search
        nums_set = set(nums)
        for i in range(len(nums)):
            if (target - nums[i]) in nums_set:
                for j in range(i + 1, len(nums)):
                    if nums[j] == target - nums[i]:
                        return [i, j]
        return [-1, -1]

    def twoSum_2(self, nums: list[int], target: int) -> list[int]:
        # Idea: Using hash map
        nums_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_map and nums_map[complement] != i:
                return [nums_map[complement], i]
            nums_map[nums[i]] = i
        return [-1, -1]
