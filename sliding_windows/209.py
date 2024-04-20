class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len, current_sum, window_start = [0] * 3

        for window_end in range(len(nums)):
            current_sum += nums[window_end]

            while current_sum >= target:
                current_len = window_end - window_start + 1
                min_len = (
                    current_len if min_len == 0 or min_len > current_len else min_len
                )
                current_sum -= nums[window_start]
                window_start += 1

        return min_len
