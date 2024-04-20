from queue import Queue


class MaxPriorityQueue:
    def __init__(self, max_size: int) -> None:
        self.length = 0
        self.arr = [0] * (max_size + 1)

    def insert(self, value: int):
        self.length += 1
        self.arr[self.length] = value

        self.swim(self.length)

    def delete_max(self):
        max_value = self.arr[1]

        self.arr[1] = self.arr[self.length]
        self.arr[self.length] = 0
        self.length -= 1
        self.sink(1)

        return max_value

    def swim(self, idx: int):
        while idx > 1 and self.arr[idx] > self.arr[idx // 2]:
            parent_node_idx = idx // 2

            temp = self.arr[idx]
            self.arr[idx] = self.arr[parent_node_idx]
            self.arr[parent_node_idx] = temp

            idx = parent_node_idx

    def sink(self, idx: int):
        while 2 * idx <= self.length:
            child_idx = 2 * idx
            if (
                child_idx < self.length
                and self.arr[child_idx] < self.arr[child_idx + 1]
            ):
                child_idx += 1

            if self.arr[idx] >= self.arr[child_idx]:
                break

            temp = self.arr[idx]
            self.arr[idx] = self.arr[child_idx]
            self.arr[child_idx] = temp

            idx = child_idx


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.pq = MaxPriorityQueue(10**6)
        self.dump_queue = Queue()
        for n in nums:
            self.pq.insert(n)

    def add(self, val: int) -> int:
        self.pq.insert(val)
        for _ in range(self.k):
            max_value = self.pq.delete_max()
            self.dump_queue.put(max_value)
        while not self.dump_queue.empty():
            self.pq.insert(self.dump_queue.get_nowait())
        return max_value
