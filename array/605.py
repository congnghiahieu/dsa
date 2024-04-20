class Solution:
    def canPlaceFlowers_1(self, flowerbed: list[int], n: int) -> bool:
        l = len(flowerbed)
        for i in range(l):
            if flowerbed[i] == 1:
                continue

            left = i - 1 < 0  # If doesn't have left, ok
            right = i + 1 >= l  # If doesn't have right, ok

            if not left and flowerbed[i - 1] == 0:
                left = True

            if not right and flowerbed[i + 1] == 0:
                right = True

            if left and right:
                flowerbed[i] = 1
                n -= 1

        return n <= 0

    def canPlaceFlowers_2(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                n -= 1

        return n <= 0
