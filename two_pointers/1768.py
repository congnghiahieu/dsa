class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ""
        l1, l2, i, j = len(word1), len(word2), 0, 0
        while i < l1 or j < l2:
            if i < l1:
                merged_word += word1[i]
                i += 1
            if j < l2:
                merged_word += word2[j]
                j += 1

        return merged_word
