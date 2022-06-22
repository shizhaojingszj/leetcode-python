from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        left = 0
        right = N - 1

        # first, last
        first, last = -1, -1

        # 求first
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
                # 结束循环
                first = mid
                break

            if nums[mid] >= target:
                # 相等时，或者大的时候，要往前面找
                right = mid - 1
            else:
                left = mid + 1

        left = 0
        right = N - 1
        # 求last
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target and (mid == N - 1 or nums[mid + 1] != target):
                # 结束循环
                last = mid
                break

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return [first, last]


def test_solution():
    input1 = [
        (dict(nums=[5, 7, 7, 8, 8, 10], target=8), [3, 4]),
        (dict(nums=[5, 7, 7, 8, 8, 10], target=6), [-1, -1]),
    ]

    for input, expect in input1:
        assert Solution().searchRange(**input) == expect, (input, expect)
