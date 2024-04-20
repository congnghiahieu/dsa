class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        l1, l2, monotonic_decrease_stack, map1 = (
            len(nums1),
            len(nums2),
            [],
            {},
        )
        ans = [-1] * l1

        for i in range(l1):
            map1[nums1[i]] = i

        for i in range(l2):
            while monotonic_decrease_stack and monotonic_decrease_stack[-1] < nums2[i]:
                num = monotonic_decrease_stack.pop()
                if map1.get(num, None) != None:
                    ans[map1[num]] = nums2[i]

            monotonic_decrease_stack.append(nums2[i])

        return ans
