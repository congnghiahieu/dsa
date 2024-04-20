class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowel, vowels = 0, {k: 0 for k in ["a", "e", "i", "o", "u"]}
        for window_end in range(len(s)):
            if s[window_end] in vowels:
                vowels[s[window_end]] += 1

            if window_end >= k - 1:
                max_vowel = max(max_vowel, sum(vowels.values()))
                if s[window_end - (k - 1)] in vowels:
                    vowels[s[window_end - (k - 1)]] -= 1
        return max_vowel
