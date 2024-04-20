from typing import Optional


class Node:
    def __init__(
        self,
        key: int,
        value: int,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
        count: int = 1,
    ) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.count = count


class BST:
    def __init__(self, root: Optional[Node] = None) -> None:
        self.root = root

    def get(self, key: int) -> Optional[int]:
        x = self.root

        while x != None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.value

        return None

    def put(self, key: int, value: int):
        return self._put(self.root, key, value)

    def _put(self, x: Optional[Node], key: int, value: int):
        if x == None:
            return Node(key, value)

        if key < x.key:
            x.left = self._put(x.left, key, value)
        elif key > x.key:
            x.right = self._put(x.right, key, value)
        else:
            x.value = value

        x.count = 1 + self._size(x.left) + self._size(x.right)

        return x

    def min_node(self):
        return self._min_node(self.root)

    def _min_node(self, x: Optional[Node]):
        while x != None and x.left != None:
            x = x.left

        return x

    def max_node(self):
        return self._max_node(self.root)

    def _max_node(self, x: Optional[Node]):
        while x != None and x.right != None:
            x = x.right

        return x

    def floor(self, key: int) -> Optional[int]:
        x = self._floor(self.root, key)
        if x == None:
            return None
        return x.key

    def _floor(self, x: Optional[Node], key: int) -> Optional[Node]:
        if x == None:
            return None

        if key == x.key:
            return x
        elif key < x.key:
            return self._floor(x.left, key)
        else:
            t = self._floor(x.right, key)
            if t != None:
                return t
            return x

    def ceil(self, key: int) -> Optional[int]:
        x = self._ceil(self.root, key)
        if x == None:
            return None
        return x.key

    def _ceil(self, x: Optional[Node], key: int) -> Optional[Node]:
        if x == None:
            return None

        if key == x.key:
            return x
        elif key > x.key:
            return self._ceil(x.right, key)
        else:
            t = self._ceil(x.left, key)
            if t != None:
                return t
            return x

    def size(self):
        return self._size(self.root)

    def _size(self, x: Optional[Node]):
        if x == None:
            return 0
        return x.count

    def rank(self, key: int):
        return self._rank(self.root, key)

    def _rank(self, x: Optional[Node], key: int):
        if x == None:
            return 0

        if key < x.key:
            return self._rank(x.left, key)
        elif key > x.key:
            return 1 + self._size(x.left) + self._rank(x.right, key)
        else:
            return self._size(x.left)

    def delete_min(self):
        self.root = self._delete_min(self.root)

    def _delete_min(self, x: Optional[Node]):
        if x == None:
            return None

        if x.left == None:
            return x.right

        x.left = self._delete_min(x.left)
        x.count = 1 + self._size(x.left) + self._size(x.right)

        return x

    def delete(self, key: int):
        self.root = self._delete(self.root, key)

    def _delete(self, x: Optional[Node], key: int):
        if x == None:
            return None

        if key < x.key:
            x.left = self._delete(x.left, key)
        elif key > x.key:
            x.right = self._delete(x.right, key)
        else:
            if x.right == None:
                return x.left
            if x.left == None:
                return x.right

            t = x
            x = self._min_node(t.right)
            x.right = self._delete_min(t.right)
            x.left = t.left

        x.count = 1 + self._size(x.left) + self._size(x.right)

        return x
