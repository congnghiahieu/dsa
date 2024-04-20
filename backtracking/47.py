class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        current_permutation: list[int] = []
        in_used: list[bool] = [False] * len(nums)
        nums.sort()

        self._permuteUnique(res, nums, current_permutation, in_used)
        return res

    def _permuteUnique(
        self,
        res: list[list[int]],
        nums: list[int],
        current_permutation: list[int],
        in_used: list[bool],
    ) -> None:
        # Check goal is reached
        if len(current_permutation) == len(nums):
            res.append([*current_permutation])
            return

        # Loop all choices
        for i in range(len(nums)):
            if in_used[i] or (i > 0 and nums[i] == nums[i - 1] and not in_used[i - 1]):
                continue

            # Make choice
            in_used[i] = True
            current_permutation.append(nums[i])
            # Backtracking
            self._permuteUnique(res, nums, current_permutation, in_used)
            # Undo choice
            in_used[i] = False
            current_permutation.pop()
