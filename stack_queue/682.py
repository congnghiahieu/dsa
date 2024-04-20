class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []

        for c in operations:
            match c:
                case "+":
                    prev1 = stack.pop()
                    prev2 = +stack.pop()
                    stack.append(prev2)
                    stack.append(prev1)
                    stack.append(prev1 + prev2)
                case "D":
                    prev = stack.pop()
                    stack.append(prev)
                    stack.append(prev * 2)
                case "C":
                    stack.pop()
                case _:
                    stack.append(int(c))

        return sum(stack)
