from bisect import bisect_right
from typing import List


class Solution:
    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        # memory not good
        res = []
        for row in matrix:
            res.extend(row)
        return sorted(res)[k - 1]

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n, beg, end = len(matrix), matrix[0][0], matrix[-1][-1]
        
        def check(m):
            i, j, cnt = 0, n-1, 0
            for i in range(n):
                while j >= 0 and matrix[i][j] > m: j -= 1
                cnt += (j + 1)
            return cnt

        def check2(m):
            cnt = 0
            for row in matrix:
                for i in row:
                    if i <= m:
                        cnt += 1
                    else:
                        break
            return cnt

        def check3(m):
            cnt = 0
            for row in matrix:
                # count number of items that are less than or equal to m
                cnt += bisect_right(row, m)
            return cnt
         
        while beg < end:
            mid = (beg + end)//2
            if check3(mid) < k:
                beg = mid + 1
            else:
                end = mid
                
        return beg


def test_solution():
    input1 = [
        (dict(matrix=[[1, 2], [1, 3]], k=2), 1),
        (
            dict(matrix=[[1, 3, 5], [6, 7, 12], [11, 14, 14]], k=3),
            5,
        ),
        (
            dict(matrix=[[1, 3, 5], [6, 7, 12], [11, 14, 14]], k=2),
            3,
        ),
        (
            dict(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8),
            13,
        ),
        (
            dict(matrix=[[-5]], k=1),
            -5,
        ),
    ]

    for input, expect in input1:
        assert Solution().kthSmallest(**input) == expect, (input, expect)
