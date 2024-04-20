from typing import Optional


# Doubly linked list, with head and tail


class Node:
    def __init__(
        self, val=0, next: Optional["Node"] = None, prev: Optional["Node"] = None
    ) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index > self.length - 1:
            return -1

        tmp = self.head
        while tmp != None and index > 0:
            index, tmp = index - 1, tmp.next

        return tmp.val if tmp != None else -1

    def addAtHead(self, val: int) -> None:
        new_head = Node(val)
        self.length += 1

        if self.head == None:
            self.head, self.tail = [new_head] * 2
            return

        new_head.next, new_head.prev = self.head, None
        self.head.prev = new_head
        self.head = new_head

    def addAtTail(self, val: int) -> None:
        new_tail = Node(val)
        self.length += 1

        if self.tail == None:
            self.head, self.tail = [new_tail] * 2
            return

        new_tail.next, new_tail.prev = None, self.tail
        self.tail.next = new_tail
        self.tail = new_tail

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        if index == self.length:
            return self.addAtTail(val)

        if self.head == None or index == 0:
            return self.addAtHead(val)

        tmp = self.head
        while tmp != None and index > 0:
            index, tmp = index - 1, tmp.next

        if not tmp:
            return

        self.length += 1
        new_node, prev_of_tmp = Node(val), tmp.prev
        tmp.prev, prev_of_tmp.next = [new_node] * 2
        new_node.prev, new_node.next = prev_of_tmp, tmp

    def deleteAtHead(self):
        if self.head == None:
            return

        self.length -= 1
        if self.head == self.tail:
            self.head, self.tail = [None] * 2
            return

        self.head.next.prev = None
        self.head = self.head.next

    def deleteAtTail(self):
        if self.tail == None:
            return

        self.length -= 1
        if self.head == self.tail:
            self.head, self.tail = [None] * 2
            return

        self.tail.prev.next = None
        self.tail = self.tail.prev

    def deleteAtIndex(self, index: int) -> None:
        if index > self.length - 1:
            return

        if index == 0:
            return self.deleteAtHead()
        if index == self.length - 1:
            return self.deleteAtTail()

        tmp = self.head
        while tmp != None and index > 0:
            index, tmp = index - 1, tmp.next

        if not tmp:
            return

        self.length -= 1
        prev_of_tmp, next_of_tmp = tmp.prev, tmp.next
        prev_of_tmp.next, next_of_tmp.prev = next_of_tmp, prev_of_tmp
