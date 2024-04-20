class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        nums = [i for i in range(1, n + 1)]
        current_combination: list[int] = []
        res: list[list[int]] = []
        self._combine(res, nums, current_combination, 0, k)
        return res

    def _combine(
        self,
        res: list[list[int]],
        nums: list[int],
        current_combination: list[int],
        start_idx: int,
        k: int,
    ):
        if len(current_combination) == k:
            res.append([*current_combination])
            return

        for idx in range(start_idx, len(nums)):
            current_combination.append(nums[idx])
            self._combine(res, nums, current_combination, idx + 1, k)
            current_combination.pop()
