class Solution:
    def insertion_sort(self, arr: list[int]):
        self._insertion_sort(arr, 0, len(arr) - 1)
        return arr

    def _insertion_sort(self, arr: list[int], l: int, h: int):
        for i in range(l + 1, h + 1):
            for j in range(i, l, -1):
                if arr[j] < arr[j - 1]:
                    temp = arr[j]
                    arr[j] = arr[j - 1]
                    arr[j - 1] = temp
                else:
                    break


print(Solution().insertion_sort([5, 2, 3, 1]))
