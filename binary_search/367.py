class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 1:
            return True

        l, h = 0, num

        while l <= h:
            m = ((h - l) // 2) + l

            if m == num / m:
                return True
            elif m > num / m:
                h = m - 1
            else:
                l = m + 1

        return False
