import random


CUT_OFF = 7


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.merge_sort(nums)
        return nums

    def merge_sort(self, nums: list[int]):
        n = len(nums)
        self._merge_sort(nums, [0] * n, 0, n - 1)

    def _merge_sort(self, nums: list[int], aux: list[int], l: int, h: int):
        # Use insertion sort for small subarrays.
        # Mergesort has too much overhead for tiny subarrays.
        # Cutoff to insertion sort for ≈ 7 items.
        if l + CUT_OFF - 1 >= h:
            self._insertion_sort(nums, l, h)
            return

        m = ((h - l) // 2) + l
        self._merge_sort(nums, aux, l, m)
        self._merge_sort(nums, aux, m + 1, h)

        if nums[m] <= nums[m + 1]:
            return

        self._merge(nums, aux, l, m, h)

    def _merge(self, nums: list[int], aux: list[int], l: int, m: int, h: int):
        for k in range(l, h + 1):
            aux[k] = nums[k]

        i, j = l, m + 1
        for k in range(l, h + 1):
            if i > m:
                nums[k] = aux[j]
                j += 1
            elif j > h:
                nums[k] = aux[i]
                i += 1
            elif aux[i] > aux[j]:
                nums[k] = aux[j]
                j += 1
            else:
                nums[k] = aux[i]
                i += 1

    def _insertion_sort(self, nums: list[int], l: int, h: int):
        for i in range(l + 1, h + 1):
            for j in range(i, l, -1):
                if nums[j] < nums[j - 1]:
                    temp = nums[j]
                    nums[j] = nums[j - 1]
                    nums[j - 1] = temp
                else:
                    break

    def quick_sort(self, nums: list[int]):
        self._shuffle(nums)
        self._quick_sort(nums, 0, len(nums) - 1)

    def _shuffle(self, nums: list[int]):
        choices = [i for i in range(len(nums))]

        for i in range(len(nums) - 1, -1, -1):
            random_idx = random.choice(choices)
            choices.pop()

            temp = nums[i]
            nums[i] = nums[random_idx]
            nums[random_idx] = temp

    def _quick_sort(self, nums: list[int], l: int, h: int):
        if l >= h:
            return

        partition_idx = self._partition(nums, l, h)
        self._quick_sort(nums, l, partition_idx - 1)
        self._quick_sort(nums, partition_idx + 1, h)

    def _partition(self, nums: list[int], l: int, h: int):
        pivot_idx, i, j = l, l + 1, h
        while True:
            while i <= h and nums[i] <= nums[pivot_idx]:
                i += 1

            while j >= l and nums[j] > nums[pivot_idx]:
                j -= 1

            if i >= j:
                break

            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        temp = nums[j]
        nums[j] = nums[pivot_idx]
        nums[pivot_idx] = temp

        return j
