class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        return self._generate("", n * 2, n, n)

    def _generate(self, current_str: str, length: int, open: int, close: int):
        if len(current_str) == length:
            return [current_str]

        res = []

        if open > 0:
            res = [*res, *self._generate(current_str + "(", length, open - 1, close)]
        if close > 0 and close > open and len(current_str) > 0:
            res = [*res, *self._generate(current_str + ")", length, open, close - 1)]

        return res
