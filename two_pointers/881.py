class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        l, r, boat = 0, len(people) - 1, 0
        while l <= r:
            if l == r:
                boat += 1
                break

            if people[l] + people[r] <= limit:
                l += 1
            r, boat = r - 1, boat + 1

        return boat
