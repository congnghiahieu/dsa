class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        i, j = 0, l - 1

        while i <= j:
            while i < l - 1 and not self.is_valid_char(s[i]):
                i += 1
            while j > 0 and not self.is_valid_char(s[j]):
                j -= 1

            if i > j:
                return (not self.is_valid_char(s[i])) == (not self.is_valid_char(s[j]))

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1
        return True

    def is_valid_char(self, c: str) -> bool:
        c = c.lower()
        return (ord("0") <= ord(c) <= ord("9")) or (ord("a") <= ord(c) <= ord("z"))

    def process_str(self, s: str) -> str:
        res = ""
        for c in s:
            if self.is_valid_char(c):
                res += c
        return res
