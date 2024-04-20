class Solution:
    def isIsomorphic1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map = {}
        for i in range(len(s)):
            if (map.get(s[i], None) == None and t[i] in map.values()) or (
                map.get(s[i], None) != None and map[s[i]] != t[i]
            ):
                return False
            else:
                map[s[i]] = t[i]
        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # The idea is that we save mapping of character via it's last corresponding index

        last_appeared_s = [-1] * 256
        last_appeared_t = [-1] * 256
        for i in range(len(s)):
            if last_appeared_s[ord(s[i])] != last_appeared_t[ord(t[i])]:
                return False

            last_appeared_s[ord(s[i])] = i
            last_appeared_t[ord(t[i])] = i
        return True
