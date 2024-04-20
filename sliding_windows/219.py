class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last_appeared_map = {}

        for i in range(len(nums)):
            if (
                last_appeared_map.get(nums[i], None) != None
                and i - last_appeared_map[nums[i]] <= k
            ):
                return True

            last_appeared_map[nums[i]] = i

        return False
