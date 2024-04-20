from queue import PriorityQueue


class Solution1:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pq = PriorityQueue()
        for point in points:
            pq.put_nowait((self.cal_distance(point), point))

        return [pq.get_nowait()[1] for _ in range(k)]

    def cal_distance(self, point: list[int]) -> float:
        return point[0] ** 2 + point[1] ** 2


class Solution2:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        self.quick_select(points, k - 1)
        return points[0:k]

    def quick_select(self, points: list[list[int]], select_idx: int):
        l, h = 0, len(points) - 1
        while l <= h:
            partition_idx = self.partition(points, l, h)
            if partition_idx < select_idx:
                l = partition_idx + 1
            elif partition_idx > select_idx:
                h = partition_idx - 1
            else:
                return points[partition_idx]

        return points[select_idx]

    def partition(self, points: list[list[int]], l: int, h: int):
        pivot_idx, i, j = l, l + 1, h
        pivot_distance = self.cal_distance(points[pivot_idx])

        while True:
            while i <= h and self.cal_distance(points[i]) <= pivot_distance:
                i += 1

            while j >= l and self.cal_distance(points[j]) > pivot_distance:
                j -= 1

            if i >= j:
                break

            temp = points[i]
            points[i] = points[j]
            points[j] = temp

        temp = points[j]
        points[j] = points[pivot_idx]
        points[pivot_idx] = temp

        return j

    def cal_distance(self, point: list[int]) -> float:
        return point[0] ** 2 + point[1] ** 2
