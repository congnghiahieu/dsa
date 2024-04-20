class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        current_subset: list[int] = []
        self._subsets(res, nums, current_subset, 0)
        return res

    def _subsets(
        self,
        res: list[list[int]],
        nums: list[int],
        current_subset: list[int],
        start_idx: int,
    ):
        res.append([*current_subset])

        for i in range(start_idx, len(nums)):
            current_subset.append(nums[i])
            self._subsets(res, nums, current_subset, i + 1)
            current_subset.pop()
