from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        if N < 3:
            return False

        i = 1
        while i <= N - 1:
            # 递增
            if arr[i] > arr[i - 1]:
                i += 1
            else:
                break
        
        # i==N说明递增的情况一直维持到头了，没有地方进行递减了
        if i == 1 or i == N:
            return False

        while i <= N - 1:
            # 递减
            if arr[i] < arr[i - 1]:
                i += 1
            else:
                break

        return i == N


def test_solution():
    input1 = [(
        dict(arr = [2,1]), False,
    ), (
        dict(arr = [3,5,5]), False,
    ), (
        dict(arr = [0,3,2,1]), True,
    )]

    for input, expect in input1:
        assert Solution().validMountainArray(**input) == expect, (input, expect)