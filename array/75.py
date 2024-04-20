class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, len(nums) - 1, 0

        while k <= j:
            if nums[k] == 0 and k != i:
                self.swap(nums, i, k)
                i += 1
            elif nums[k] == 2 and k != j:
                self.swap(nums, j, k)
                j -= 1
            else:
                k += 1

    def swap(self, nums: list[int], idx1: int, idx2: int):
        temp = nums[idx1]
        nums[idx1] = nums[idx2]
        nums[idx2] = temp
