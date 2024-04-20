class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res: list[list[int]] = []
        current_combination: list[int] = []
        current_sum = 0
        candidates.sort()

        self._combinationSum2(
            res, candidates, current_combination, current_sum, 0, target
        )

        return res

    def _combinationSum2(
        self,
        res: list[list[int]],
        candidates: list[int],
        current_combination: list[int],
        current_sum: int,
        start_idx: int,
        target: int,
    ):
        if current_sum > target:
            return

        if current_sum == target:
            res.append([*current_combination])
            return

        for i in range(start_idx, len(candidates)):
            if i > start_idx and candidates[i] == candidates[i - 1]:
                continue

            current_sum += candidates[i]
            current_combination.append(candidates[i])

            self._combinationSum2(
                res,
                candidates,
                current_combination,
                current_sum,
                i + 1,
                target,
            )

            current_sum -= candidates[i]
            current_combination.pop()
