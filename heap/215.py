from queue import PriorityQueue


class Solution1:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pq, ans = PriorityQueue(), 0
        for n in nums:
            pq.put_nowait((-n, n))
        for _ in range(k):
            ans = pq.get_nowait()[1]
        return ans


class Solution2:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return self.quick_select(nums, (len(nums) - 1) - (k - 1))

    def quick_select(self, nums: list[int], select_idx: int):
        l, h = 0, len(nums) - 1

        while l < h:
            partition_idx = self.partition(nums, l, h)
            if partition_idx < select_idx:
                l = partition_idx + 1
            elif partition_idx > select_idx:
                h = partition_idx - 1
            else:
                return nums[partition_idx]

        return nums[select_idx]

    def partition(self, nums: list[int], l: int, h: int):
        pivot_idx, i, j = l, l + 1, h
        while True:
            while i <= h and nums[i] <= nums[pivot_idx]:
                i += 1

            while j >= l and nums[j] > nums[pivot_idx]:
                j -= 1

            if i >= j:
                break

            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        temp = nums[j]
        nums[j] = nums[pivot_idx]
        nums[pivot_idx] = temp

        return j
