from collections import deque


# To implement a monotonic stack, stack is enought but we can also use deque
# Otherwise to implment a monotonic queue, we have to use deque


def increasing_monotonic_stack(arr: list[int]):
    # q = deque()
    q = []
    for i in range(len(arr)):
        while q and q[-1] > arr[i]:
            q.pop()
        q.append(arr[i])
    return q


def run_increasing_monotonic_stack():
    arr = [5, 6, 72, 3, 1, 65, -1, 5, 256, 1654, 2, 7, -6]
    q = increasing_monotonic_stack(arr)
    for i in q:
        print(i, end=" ")


def decreasing_monotonic_stack(arr: list[int]):
    # q = deque()
    q = []
    for i in range(len(arr)):
        while q and q[-1] < arr[i]:
            q.pop()
        q.append(arr[i])
    return q


def run_decreasing_monotonic_stack():
    arr = [5, 6, 72, 3, 1, 65, -1, 5, 256, 1654, 2, 7, -6]
    q = decreasing_monotonic_stack(arr)
    for i in q:
        print(i, end=" ")


dq = deque()
