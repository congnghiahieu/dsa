class Solution:
    def binary_search_recursive(self, arr: list[int], target: int):
        return self._binary_search_recursive(arr, target, 0, len(arr) - 1)

    def _binary_search_recursive(self, arr: list[int], target: int, l: int, h: int):
        if l > h:
            return -1

        m = ((h - l) // 2) + l
        if arr[m] > target:
            return self._binary_search_recursive(arr, target, l, m - 1)
        elif arr[m] < target:
            return self._binary_search_recursive(arr, target, m + 1, h)
        else:
            return m

    def binary_search_iterative(self, arr: list[int], target):
        l, h = 0, len(arr) - 1
        while l <= h:
            m = ((h - l) // 2) + l
            if arr[m] < target:
                l = m + 1
            elif arr[m] > target:
                h = m - 1
            else:
                return m
        return -1
