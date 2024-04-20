class Solution:
    def removeStars_1(self, s: str) -> str:
        # Idea: Not using stack, counting star and loop from end to start
        star_count, res = 0, ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "*":
                star_count += 1
                continue

            if star_count:
                star_count -= 1
            else:
                res += s[i]

        return res[::-1]

    def removeStars_2(self, s: str) -> str:
        # Idea: using stack to store charater. If meet star, pop last character
        str_stack = []
        for c in s:
            if c == "*" and str_stack:
                str_stack.pop()
            else:
                str_stack.append(c)
        return "".join(str_stack)
