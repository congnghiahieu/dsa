from queue import PriorityQueue


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        pq = PriorityQueue()
        for s in stones:
            pq.put_nowait((-s, s))

        while not pq.empty():
            first_value = pq.get_nowait()[1]
            if pq.empty():
                return first_value
            second_value = pq.get_nowait()[1]

            if first_value != second_value:
                new_value = first_value - second_value
                pq.put_nowait((-new_value, new_value))

        return 0
