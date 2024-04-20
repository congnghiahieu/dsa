class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        current_permutation: list[int] = []
        in_used: list[bool] = [False] * len(nums)
        self._permute(res, nums, current_permutation, in_used)
        return res

    def _permute(
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
            if not in_used[i]:
                # Make choice
                in_used[i] = True
                current_permutation.append(nums[i])
                # Backtracking
                self._permute(res, nums, current_permutation, in_used)
                # Undo choice
                in_used[i] = False
                current_permutation.pop()
