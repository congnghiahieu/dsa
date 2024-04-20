from queue import Queue


class MyStack_1:
    # Using 2 queue
    def __init__(self):
        self.main_queue = Queue()
        self.tmp_queue = Queue()

    def push(self, x: int) -> None:
        while not self.main_queue.empty():
            self.tmp_queue.put(self.main_queue.get_nowait())

        self.main_queue.put(x)

        while not self.tmp_queue.empty():
            self.main_queue.put(self.tmp_queue.get_nowait())

    def pop(self) -> int:
        return self.main_queue.get_nowait()

    def top(self) -> int:
        t = self.main_queue.get_nowait()
        while not self.main_queue.empty():
            self.tmp_queue.put(self.main_queue.get_nowait())

        self.main_queue.put(t)

        while not self.tmp_queue.empty():
            self.main_queue.put(self.tmp_queue.get_nowait())
        return t

    def empty(self) -> bool:
        return self.main_queue.empty()


class MyStack_2:
    # Using 1 queue
    def __init__(self):
        self.queue = Queue()
        self.size = 0

    def push(self, x: int) -> None:
        self.queue.put_nowait(x)
        for _ in range(self.size):
            self.queue.put_nowait(self.queue.get_nowait())
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return self.queue.get_nowait()

    def top(self) -> int:
        t = self.queue.get_nowait()
        self.queue.put_nowait(t)
        for _ in range(self.size - 1):
            self.queue.put_nowait(self.queue.get_nowait())
        return t

    def empty(self) -> bool:
        return self.size == 0
