import random


class Solution:
    def knuth_shuffle_increment(self, arr: list[int]):
        # This implementation increment range of random
        choices = []
        for i in range(len(arr)):
            # Randomly choose a `r` number that between 0 and i
            choices.append(i)
            r = random.choice(choices)
            # Swap arr[r] with arr[i]
            temp = arr[i]
            arr[i] = arr[r]
            arr[r] = temp

    def knuth_shuffle_decrement(self, arr: list[int]):
        # This implementation decrement range of random
        choices = [i for i in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            # Randomly choose a `r` number that between 0 and 1
            r = random.choice(choices)
            choices.pop()
            # Swap arr[i] with arr[r]
            temp = arr[i]
            arr[i] = arr[r]
            arr[r] = temp
