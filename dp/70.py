class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = {}
        stairs[1], stairs[2] = 1, 2
        for i in range(3, n + 1):
            stairs[i] = stairs[i - 1] + stairs[i - 2]
        return stairs[n]
