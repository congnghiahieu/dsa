class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        parts = s.split(" ")

        if len(parts) != len(pattern):
            return False

        map1, map2 = (
            {c: -1 for c in pattern},
            {part: -1 for part in parts},
        )
        for i in range(len(pattern)):
            if map1[pattern[i]] != map2[parts[i]]:
                return False
            map1[pattern[i]] = i
            map2[parts[i]] = i

        return True
