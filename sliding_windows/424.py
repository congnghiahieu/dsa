class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency, window_start, max_count, max_length = [0] * 26, 0, 0, 0

        for window_end in range(len(s)):
            frequency[ord(s[window_end]) - ord("A")] += 1
            max_count = max(max_count, frequency[ord(s[window_end]) - ord("A")])

            while window_end - window_start + 1 - max_count > k:
                frequency[ord(s[window_start]) - ord("A")] -= 1
                window_start -= 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length
