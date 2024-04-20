class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        decrease_stack, ans = [], [0] * len(temperatures)

        for i in range(len(temperatures)):
            while decrease_stack and decrease_stack[-1][1] < temperatures[i]:
                cooler_day_idx = decrease_stack.pop()[0]
                ans[cooler_day_idx] = i - cooler_day_idx

            decrease_stack.append([i, temperatures[i]])

        return ans
