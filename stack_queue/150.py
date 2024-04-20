class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operand_stack = []

        for c in tokens:
            if c not in ["+", "-", "*", "/"]:
                operand_stack.append(int(c))
                continue

            second_num, first_num = operand_stack.pop(), operand_stack.pop()
            match c:
                case "+":
                    operand_stack.append(first_num + second_num)
                case "-":
                    operand_stack.append(first_num - second_num)
                case "*":
                    operand_stack.append(first_num * second_num)
                case "/":
                    operand_stack.append(int(first_num / second_num))

        return operand_stack.pop()
