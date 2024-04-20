class Solution:
    def reverseString_1(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            tmp = s[r]
            s[r] = s[l]
            s[l] = tmp
            l, r = l + 1, r - 1
