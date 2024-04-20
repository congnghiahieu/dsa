class Solution:
    def plusOne_1(self, digits: list[int]) -> list[int]:
        # Loop in reversed order
        l = len(digits)
        for i in range(l - 1, -1, -1):
            # Add one digit for last number only
            if i == l - 1:
                digits[i] += 1

            # If not equal 10 then break
            if digits[i] % 10 != 0:
                break

            # Equal 10
            digits[i] = 0
            if i != 0:
                digits[i - 1] += 1
            else:
                digits.insert(0, 1)
        return digits

    def plusOne_2(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1, *digits]
