class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def coinChange(self, coins: list[int], amount: int) -> int:
        min_way = -1

        if amount == 0:
            return 0

        if amount in coins:
            return 1

        for coin in coins:
            sub_problem = amount - coin

            if sub_problem < 0:
                continue

            sub_way = -1
            if sub_problem in self.memo:
                sub_way = self.memo[sub_problem]
            else:
                sub_way = self.coinChange(coins, sub_problem)

            self.memo[sub_problem] = sub_way

            if sub_way != -1 and (min_way == -1 or sub_way + 1 < min_way):
                min_way = sub_way + 1

        self.memo[amount] = min_way

        return min_way
