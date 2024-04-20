class Solution:
    def decodeString(self, s: str) -> str:
        quantity_stack, str_stack, ans = [0], [""], ""

        for c in s:
            if ord("0") <= ord(c) <= ord("9"):
                quantity_stack[-1] = quantity_stack[-1] * 10 + int(c)
            elif ord("a") <= ord(c) <= ord("z"):
                if str_stack:
                    str_stack[-1] += c
                else:
                    ans += c
            elif c == "[":
                str_stack.append("")
                quantity_stack.append(0)
            else:
                char_list, quantity = str_stack.pop(), 0

                while quantity_stack and quantity_stack[-1] == 0:
                    quantity_stack.pop()

                quantity = quantity_stack.pop()

                repeated_str = "".join([char_list for _ in range(quantity)])
                if str_stack:
                    str_stack[-1] += repeated_str
                else:
                    ans += repeated_str
                """"""

        return ans


s = "3[a]2[bc]"
o = "aaabcbc"
print(Solution().decodeString(s) == o)
