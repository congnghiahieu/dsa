class StockSpanner:

    def __init__(self):
        self.price_stack = []

    def next(self, price: int) -> int:
        count, i = 1, len(self.price_stack) - 1

        while i >= 0 and self.price_stack[i] <= price:
            i, count = i - 1, count + 1

        self.price_stack.append(price)

        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
