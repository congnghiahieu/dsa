class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        stairs, l = {}, len(cost)
        stairs[0], stairs[1] = 0, 0
        for i in range(2, l + 1):
            stairs[i] = min(cost[i - 1] + stairs[i - 1], cost[i - 2] + stairs[i - 2])
        return stairs[l]
