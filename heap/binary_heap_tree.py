class MaxBinaryHeapTree:
    def __init__(self, max_size: int):
        # arr start index at 1
        self.length = 0
        self.arr = [0] * (max_size + 1)

    def insert(self, value: int):
        self.length += 1
        self.arr[self.length] = value
        # Swim new node up
        self.swim(self.length)

    def delete_max(self) -> int:
        max_value = self.arr[1]

        # Swap largest node (first node) with the last node
        self.arr[1] = self.arr[self.length]
        self.arr[self.length] = 0
        self.length -= 1
        # Sink the last node
        self.sink(1)

        return max_value

    def swim(self, idx: int):
        # If greater than parent node, swap
        while idx > 1 and self.arr[idx] > self.arr[idx // 2]:
            parent_node_idx = idx // 2
            temp = self.arr[idx]
            self.arr[idx] = self.arr[parent_node_idx]
            self.arr[parent_node_idx] = temp
            # Continue to swim up to higher level
            idx = parent_node_idx

    def sink(self, idx: int):
        while 2 * idx <= self.length:
            # Get larger child
            child_idx = 2 * idx
            if (
                child_idx < self.length
                and self.arr[child_idx] < self.arr[child_idx + 1]
            ):
                child_idx += 1
            # If no child greater than parent, stop
            if self.arr[idx] >= self.arr[child_idx]:
                break
            # Swap parent with child
            temp = self.arr[idx]
            self.arr[idx] = self.arr[child_idx]
            self.arr[child_idx] = temp
            # Continue to sink down to lower level
            idx = child_idx
