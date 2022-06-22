from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers
        left = 0
        right = len(height) - 1

        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right])*(right - left)) 

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


def test_solution():
    input1 = [(
        dict(height = [1,8,6,2,5,4,8,3,7]), 49,
    )]

    for input, expect in input1:
        assert Solution().maxArea(**input) == expect, (input, expect)
