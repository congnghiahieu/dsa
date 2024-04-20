from typing import Optional


class MyCircularQueue:

    def __init__(self, k: int):
        self.length = k
        self.arr: list[Optional[int]] = [None] * k
        self.front, self.rear = [-1] * 2

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.front, self.rear = [0] * 2
            self.arr[self.front] = value
            return True

        self.rear = (self.rear + 1) % self.length
        self.arr[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.arr[self.front] = None

        # One element left
        if self.front == self.rear:
            self.front, self.rear = [-1] * 2
            return True

        # More than one element left
        self.front = (self.front + 1) % self.length
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1 and self.rear == -1

    def isFull(self) -> bool:
        return (
            not self.isEmpty()
            and (self.rear - self.front == self.length - 1)
            or self.front - self.rear == 1
        )


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
