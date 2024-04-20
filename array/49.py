from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group_map: dict[str, list[str]] = defaultdict(list)
        for s in strs:
            group_map[self.get_key(s)].append(s)
        return [v for v in group_map.values()]

    def get_key(self, s: str):
        character_a_unicode, frequency = ord("a"), [0] * 26
        for c in s:
            frequency[ord(c) - character_a_unicode] += 1
        return "".join(
            [
                chr(i + character_a_unicode) + str(frequency[i])
                for i in range(len(frequency))
                if frequency[i] != 0
            ]
        )

    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        group_map: dict[tuple, list[str]] = defaultdict(list)
        for s in strs:
            group_map[self.get_key2(s)].append(s)
        return [v for v in group_map.values()]

    def get_key2(self, s: str):
        key = [0] * 26

        for c in s:
            key[ord(c) - ord("a")] += 1

        return tuple(key)
