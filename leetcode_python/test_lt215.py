import heapq
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.heap_method(nums, k)

    def bruteforce(self, nums, k):
        return sorted(nums, reverse=True)[k - 1]

    def heap_method(self, nums, k):
        # min heap
        # heapify => O(n)
        heapq.heapify(nums)
        for _ in range(len(nums) - k + 1):
            result = heapq.heappop(nums)

        return result

    def quick_select(self, nums, k):
        N = len(nums)

        left = 0
        right = N - 1

        def logic(left, right):
            pivot_idx = self.random_pivot(left, right)
            self.swap(nums, pivot_idx, right)

            # 找到该值的rank
            val = nums[right]
            mid = 0
            for i in range(right):
                if nums[i] < val:
                    # 如果小于该值，就放到当前mid指定的位置
                    self.swap(nums, mid, i)
                    mid += 1
            # 最终swap回来
            self.swap(nums, mid, right)
            # 最终mid的值跟k进行比较
            return mid

        while left <= right:
            mid = logic(left, right)
            if mid < k:
                left = mid
                # k not change
            elif mid == k:
                return nums[mid]
            else:
                # 问题有变化
                right = mid
                k = k - (N - mid)

    def random_pivot(self, lo, hi):
        # inclusive
        return random.randint(lo, hi)

    def swap(self, nums, first, second):
        nums[first], nums[second] = nums[second], nums[first]


def test_solution():
    input1 = [
        (
            dict(nums=[3, 2, 1, 5, 6, 4], k=2),
            5,
        ),
        (
            dict(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4),
            4,
        ),
    ]

    for input, expect in input1:
        assert Solution().findKthLargest(**input) == expect, (input, expect)
