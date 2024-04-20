CUT_OFF = 7


class Solution:
    def merge_sort(self, arr: list[int]):
        n = len(arr)
        return self._merge_sort(arr, [0] * n, 0, n - 1)

    def _merge_sort(self, arr: list[int], aux: list[int], l: int, h: int):
        # Use insertion sort for small subarrays.
        # Mergesort has too much overhead for tiny subarrays.
        # Cutoff to insertion sort for ≈ 7 items.
        if l + CUT_OFF - 1 >= h:
            self._insertion_sort(arr, l, h)
            return

        m = ((h - l) // 2) + 1
        self._merge_sort(arr, aux, l, m)
        self._merge_sort(arr, aux, m + 1, h)

        if arr[m] <= arr[m + 1]:
            return

        self._merge_two_sorted_array(arr, aux, l, h, m)

    def _merge_two_sorted_array(
        self, arr: list[int], aux: list[int], l: int, h: int, m: int
    ):
        for k in range(l, h + 1):
            aux[k] = arr[k]

        i, j = l, m + 1
        for k in range(l, h + 1):
            if i > m:
                arr[k] = aux[j]
                j += 1
            elif j > h:
                arr[k] = aux[i]
                i += 1
            elif aux[i] > aux[j]:
                arr[k] = aux[j]
                j += 1
            else:
                arr[k] = aux[i]
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
