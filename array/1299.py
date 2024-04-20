class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_right = 0
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                max_right = arr[i]
                arr[i] = -1
            else:
                tmp = arr[i]
                arr[i] = max_right
                if tmp > max_right:
                    max_right = tmp
        return arr
