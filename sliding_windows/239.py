from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        decreasing_dq, res = deque(), []

        for window_end in range(len(nums)):

            while decreasing_dq and decreasing_dq[-1] < nums[window_end]:
                decreasing_dq.pop()

            decreasing_dq.append(nums[window_end])

            if window_end >= k - 1:
                res.append(decreasing_dq[0])

                if nums[window_end - (k - 1)] == decreasing_dq[0]:
                    decreasing_dq.popleft()

        return res


print(Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
