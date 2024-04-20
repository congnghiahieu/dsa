class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        valid_chars = ["b", "a", "l", "o", "n"]
        freq = {key: 0 for key in valid_chars}
        for c in text:
            if c in valid_chars:
                freq[c] += 1
        freq["l"] //= 2
        freq["o"] //= 2
        return min(freq.values())
