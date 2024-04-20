class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res: list[list[int]] = []
        current_combination: list[int] = []
        current_sum = 0

        self._combinationSum(
            res,
            candidates,
            current_combination,
            current_sum,
            0,
            len(candidates) - 1,
            target,
        )

        return res

    def _combinationSum(
        self,
        res: list[list[int]],
        candidates: list[int],
        current_combination: list[int],
        current_sum: int,
        start_idx: int,
        end_idx: int,
        target: int,
    ):
        if current_sum > target:
            return

        if current_sum == target:
            res.append([*current_combination])
            return

        for i in range(start_idx, end_idx + 1):
            current_sum += candidates[i]
            current_combination.append(candidates[i])

            self._combinationSum(
                res,
                candidates,
                current_combination,
                current_sum,
                i,
                end_idx,
                target,
            )

            current_sum -= candidates[i]
            current_combination.pop()
