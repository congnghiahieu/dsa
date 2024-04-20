class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack: list[str] = []

        for c in s:
            if stack and stack[-1][-1] == c:
                stack[-1] += c
                if len(stack[-1]) == k:
                    stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
