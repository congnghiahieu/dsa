class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_str, min_length, window_start, t_map = "", -1, 0, {}

        for c in t:
            t_map[c] = t_map.get(c, 0) + 1

        for window_end in range(len(s)):
            if s[window_end] in t_map:
                t_map[s[window_end]] -= 1

            while all(v <= 0 for v in t_map.values()):
                current_length = window_end - window_start + 1
                if min_length == -1 or current_length < min_length:
                    min_length = current_length
                    ans_str = s[window_start : window_end + 1]

                if s[window_start] in t_map:
                    t_map[s[window_start]] += 1

                window_start += 1

        return ans_str


s = "a"
t = "aa"
print(Solution().minWindow(s, t))
