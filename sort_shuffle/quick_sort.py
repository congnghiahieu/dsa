import random


class Solution:
    def quick_sort(self, arr: list[int]):
        self._shuffle(arr)  # Shuffle needed for performance guarantee
        return self._quick_sort(arr, 0, len(arr) - 1)

    def _shuffle(self, arr: list[int]):
        # Knuth (Fisher - Yates) Shuffle
        n = len(arr)
        choices = [i for i in range(n)]
        for i in range(n - 1, -1, -1):
            # Pick a random `r` number between 0 and i
            r = random.choice(choices)
            choices.pop()
            # Swap arr[i] and arr[r]
            temp = arr[i]
            arr[i] = arr[r]
            arr[r] = temp

    def _quick_sort(self, arr: list[int], l: int, h: int):
        if l >= h:
            return

        partition_idx = self._partition_with_pivot_at_the_start(arr, l, h)
        self._quick_sort(arr, l, partition_idx - 1)
        self._quick_sort(arr, partition_idx + 1, h)

    def _partition_with_pivot_at_the_start(self, arr: list[int], l: int, h: int) -> int:
        # This is the algorithm if we choose pivot at the start
        # Choose the position of pivot, at the start or end or other position really matter

        pivot, i, j = l, l + 1, h
        while True:
            while i <= h and arr[i] <= arr[pivot]:
                i += 1

            while j >= l and arr[j] > arr[pivot]:
                j -= 1

            if i >= j:
                break

            # Swap at index i and j
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

        # Swap at index pivot and j
        temp = arr[pivot]
        arr[pivot] = arr[j]
        arr[j] = temp

        return j

    def _partition_with_pivot_at_the_end(self, arr: list[int], l: int, h: int) -> int:
        # This is the algorithm if we choose pivot at the end
        # Choose the position of pivot, at the start or end or other position really matter

        pivot, pivot_idx = h, l

        for i in range(l, h):
            if arr[i] < arr[pivot]:
                # Swap element at index pivot_idx and i
                temp = arr[i]
                arr[i] = arr[pivot_idx]
                arr[pivot_idx] = temp

                # Increment pivot_idx by one
                pivot_idx += 1

        # Swap element at index pivot and pivot_idx
        temp = arr[pivot]
        arr[pivot] = arr[pivot_idx]
        arr[pivot_idx] = temp

        return pivot_idx
