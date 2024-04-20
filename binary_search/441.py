class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, h, ans = 0, n, 0
        while l <= h:
            rows = ((h - l) // 2) + l
            coins_needed = (rows * (rows + 1)) // 2
            if coins_needed > n:
                h = rows - 1
            else:
                l, ans = rows + 1, rows
        return ans
