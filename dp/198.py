class Solution:
    def rob(self, nums: list[int]) -> int:
        max_money, max_money_at_houses = nums[0], {0: nums[0]}

        for i in range(1, len(nums)):
            max_money_at_houses[i] = nums[i] + max(
                [max_money_at_houses[j] for j in range(0, i - 1)], default=0
            )
            max_money = max(max_money, max_money_at_houses[i])

        return max_money
