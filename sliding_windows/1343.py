class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        count, window_sum = [0] * 2
        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            if window_end >= k - 1:
                if window_sum >= threshold * k:
                    count += 1
                window_sum -= arr[window_end - (k - 1)]
        return count
