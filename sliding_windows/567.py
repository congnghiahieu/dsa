class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size, s1_map = len(s1), {}

        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1

        for window_end in range(len(s2)):
            if s2[window_end] in s1_map:
                s1_map[s2[window_end]] -= 1

            if window_end >= window_size - 1:
                if all([v == 0 for v in s1_map.values()]):
                    return True
                if s2[window_end - (window_size - 1)] in s1_map:
                    s1_map[s2[window_end - (window_size - 1)]] += 1
        return False
