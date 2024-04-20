import random


class Solution:
    def quick_select(self, arr: list[int], k: int):

        self._shuffle(arr)
        l, h = 0, len(arr) - 1

        while l < h:
            pivot_idx = self._partition(arr, l, h)
            if pivot_idx < k:
                l = pivot_idx + 1
            elif pivot_idx > k:
                h = pivot_idx - 1
            else:
                return arr[pivot_idx]

        return arr[k]

    def _shuffle(self, arr: list[int]):
        choices = []
        for i in range(len(arr)):
            choices.append(i)
            r = random.choice(choices)

            temp = arr[i]
            arr[i] = arr[r]
            arr[r] = temp

    def _partition(self, arr: list[int], l: int, h: int):
        pivot, i, j = l, l + 1, h

        while True:
            while i <= h and arr[i] <= arr[pivot]:
                i += 1
            while j >= l and arr[j] > arr[pivot]:
                j += 1

            if i >= j:
                break

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

        temp = arr[pivot]
        arr[pivot] = arr[j]
        arr[j] = temp

        return j
