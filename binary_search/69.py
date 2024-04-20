class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        l, h, ans = 0, x, 0
        while l <= h:
            m = ((h - l) // 2) + l
            if m > x // m:
                h = m - 1
            else:
                l, ans = m + 1, m
        return ans
