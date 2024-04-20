class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length, window_start, char_map = 0, 0, {}

        for window_end in range(len(s)):
            char_map[s[window_end]] = char_map.get(s[window_end], 0) + 1

            while char_map[s[window_end]] > 1:
                char_map[s[window_start]] -= 1
                window_start += 1

            max_length = max(window_end - window_start + 1, max_length)
        return max_length
