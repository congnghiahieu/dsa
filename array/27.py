class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        appeared, i, j = 0, 0, len(nums) - 1

        while i <= j:
            if nums[i] == val:
                appeared += 1

                while j > i and nums[j] == val:
                    appeared += 1
                    j -= 1

                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

                j -= 1

            i += 1

        return len(nums) - appeared


nums = [1]
val = 1
print(Solution().removeElement(nums, val))
