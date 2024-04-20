class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        current_subset: list[int] = []
        nums.sort()
        self._subsetsWithDup(res, nums, current_subset, 0)
        return res

    def _subsetsWithDup(
        self,
        res: list[list[int]],
        nums: list[int],
        current_subset: list[int],
        start_idx: int,
    ):
        res.append([*current_subset])

        for i in range(start_idx, len(nums)):
            # skip duplicates
            if i > start_idx and nums[i] == nums[i - 1]:
                continue

            current_subset.append(nums[i])
            self._subsetsWithDup(res, nums, current_subset, i + 1)
            current_subset.pop()
