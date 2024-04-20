class Solution:
    def strStr_1(self, haystack: str, needle: str) -> int:
        # Idea: Compare each character (normal idea)
        # Time: O(m * n) (m is length of haystack, n is length of needle)

        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i -= j - 1
                j = 0

            if j == len(needle):
                return i - j
        return -1

    def strStr_2(self, haystack: str, needle: str) -> int:
        # Knuth-Moris-Patt String Search
        # Idea: never look back cursor (i) in haystack, just look back cursor (j) in needle. Check for suffix and prefix to decide where we take cursor (j) back
        # Time: O(m + n) (m is length of haystack, n is length of needle)

        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i -= j - 1
                j = 0

            if j == len(needle):
                return i - j
        return -1
