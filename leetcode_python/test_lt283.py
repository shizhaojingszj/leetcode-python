from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        number0 = 0
        numberNot0 = 0

        N = len(nums)
        # 第一次循环进行计数
        for i in range(N):
            if nums[i] == 0:
                number0 += 1
            else:
                nums[numberNot0] = nums[i]
                numberNot0 += 1
        # 把后面的值进行0值化
        for j in range(numberNot0, N):
            nums[j] = 0

        return nums


def test_solution():
    input1 = [(
        dict(nums = [0,1,0,3,12]),
        [1,3,12,0,0],
    )]

    for input, expect in input1:
        assert Solution().moveZeroes(**input) == expect, (input, expect)