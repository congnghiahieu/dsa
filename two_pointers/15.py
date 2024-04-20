class Solution1:
    """This solution use sort, solve two sum by 2 poiter and already AC"""

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            front, rear, target = i + 1, len(nums) - 1, -nums[i]
            l, h = front, rear
            while l < h:
                two_sum = nums[l] + nums[h]
                if two_sum > target:
                    h -= 1
                elif two_sum < target:
                    l += 1
                else:
                    if (l == front or nums[l] != nums[l - 1]) and (
                        h == rear or nums[h] != nums[h + 1]
                    ):
                        res.append([nums[i], nums[l], nums[h]])
                    l += 1
                    h -= 1

        return res


class Solution2:
    """This solution use sort, solve two sum by hash but not AC yet"""

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for two_sum_ans in self.two_sum(nums, i + 1, -nums[i]):
                ans.append([nums[i], *two_sum_ans])
        return ans

    def two_sum(self, nums: list[int], l: int, target: int) -> list[list[int]]:
        nums_map, ans = {}, []
        for i in range(l, len(nums)):
            if i > l + 1 and nums[i] == nums[i - 2]:
                continue

            complement = target - nums[i]
            if complement in nums_map and nums_map[complement] != i:
                ans.append([nums[i], complement])

            nums_map[nums[i]] = i
        return ans
