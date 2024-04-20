class Solution:
    def selection_sort(self, arr: list[int]) -> list[int]:
        l = len(arr)
        for i in range(l - 1):
            min_index = i
            for j in range(i + 1, l):
                if arr[j] < arr[min_index]:
                    min_index = j
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp
        return arr
