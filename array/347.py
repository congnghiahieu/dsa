class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency: dict[int, int] = {}
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1

        return self.quick_select_from_top_k_biggest(frequency, k)

    def quick_select_from_top_k_biggest(self, nums: list[int], k: int):
        top_k_biggest, last_idx = [], len(nums) - 1
        l, h = (
            0,
            last_idx,
        )

        while l <= h:
            partition_idx = self._partition(nums, l, h)
            if partition_idx >= last_idx - (k - 1):
                top_k_biggest.append(nums[partition_idx])

            if partition_idx < last_idx:
                l = partition_idx + 1
            elif partition_idx > last_idx:
                h = partition_idx - 1
            else:
                break

        return top_k_biggest

    def _partition(self, nums: list[int], l: int, h: int):
        pivot_idx, i, j = l, l + 1, h
        while True:
            while i <= h and nums[i] <= nums[pivot_idx]:
                i += 1

            while j >= l and nums[j] > nums[pivot_idx]:
                j -= 1

            if i >= j:
                break

            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp

        temp = nums[j]
        nums[j] = nums[pivot_idx]
        nums[pivot_idx] = temp

        return j
