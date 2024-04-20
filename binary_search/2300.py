class Solution:
    def successfulPairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:
        potions.sort()

        l_s, l_p = len(spells), len(potions)
        ans = [0] * l_s

        for i in range(l_s):
            satisfy_idx = self.search_satisfy_idx(potions, spells[i], success)
            if satisfy_idx != -1:
                ans[i] = l_p - satisfy_idx

        return ans

    def search_satisfy_idx(self, potions: list[int], current_spell: int, success: int):
        l, h = 0, len(potions) - 1
        while l <= h:
            m = ((h - l) // 2) + l
            if potions[m] * current_spell < success:
                return m
            else:
                

        return -1
