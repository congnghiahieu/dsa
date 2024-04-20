class Solution:
    def validPalindrome_1(self, s: str) -> bool:
        # Idea: Using two pointer only
        # The mismatch character can cause wrong position in either left or right, so we have to choose between move left or right.
        # The idea is that if we choose move right at first and it fails, retry choosing move left
        deleted, retry, r_chosen = [False] * 3
        old_l, old_r = [-1] * 2
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] == s[r]:
                l, r = l + 1, r - 1
                continue

            if not deleted:
                deleted = True
                old_l, old_r = l, r
                if s[l] == s[r - 1]:
                    r -= 1
                    r_chosen = True
                else:
                    l += 1
            else:
                if retry:
                    return False

                l, r, retry = old_l, old_r, True
                if r_chosen:
                    l += 1
                else:
                    r -= 1
        return True

    def validPalindrome_2(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                move_l_str, move_r_str = s[l + 1 : r + 1], s[l:r]
                return move_l_str == move_l_str[::-1] or move_r_str == move_r_str[::-1]
            l, r = l + 1, r - 1
        return True


s = "ececabbacec"
Solution().validPalindrome_1(s)
