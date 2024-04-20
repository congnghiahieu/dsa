class Solution:
    def isAnagram_1(self, s: str, t: str) -> bool:
        # Idea: sort 2 string and compare
        # 2 anagram has same word count but in different order. If we sort them, they will have same order and will be the same string
        return sorted(s) == sorted(t)

    def isAnagram_2(self, s: str, t: str) -> bool:
        # Idea: Using a hash to count frequency, if frequency is not the same => not anagram
        # Instead of using 2 map to count frequency, we use only 1. For one string we increment frequency and decrement frequency for the other

        if len(s) != len(t):
            return False

        def increment(dic: dict, key: str, amount: int):
            if dic.get(key, None) == None:
                dic[key] = amount
            else:
                dic[key] += amount

        frequency = {}
        for i in range(len(s)):
            increment(frequency, s[i], 1)
            increment(frequency, t[i], -1)

        for value in frequency.values():
            if value != 0:
                return False
        return True

    def isAnagram_3(self, s: str, t: str) -> bool:
        # Idea: Using a hash to count frequency, if frequency is not the same => not anagram
        # Instead of using map as hash table, we use array as hash table
        # Because characters range from 'a' -> 'z', so we utilize their UNICODE point (ASCII) from 97 -> 122 (26 character), we mapping from (97,122) to (0,25)

        if len(s) != len(t):
            return False

        frequency = [0] * 26
        for i in range(len(s)):
            frequency[ord(s[i]) - ord("a")] += 1
            frequency[ord(t[i]) - ord("a")] -= 1

        for f in frequency:
            if f != 0:
                return False
        return True
