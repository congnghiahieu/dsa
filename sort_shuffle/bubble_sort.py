class Solution:
    def bubble_sort(self, arr: list[int]) -> list[int]:
        l = len(arr)
        for i in range(l - 1, 0, -1):
            swapped = False

            for j in range(0, i):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
                    swapped = True

            if not swapped:
                break
        return arr
