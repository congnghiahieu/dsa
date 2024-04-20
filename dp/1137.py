class Solution:
    def tribonacci(self, n: int) -> int:
        fib = {}
        fib[0], fib[1], fib[2] = 0, 1, 1
        for i in range(3, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2] + fib[i - 3]
        return fib[n]
