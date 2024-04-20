class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l = len(nums)
        prefix_product, suffix_product = [1] * l, [1] * l

        for i in range(1, l):
            prefix_product[i] = nums[i - 1] * prefix_product[i - 1]
        for i in range(l - 2, -1, -1):
            suffix_product[i] = nums[i + 1] * suffix_product[i + 1]

        return [
            prefix * suffix for prefix, suffix in zip(prefix_product, suffix_product)
        ]
