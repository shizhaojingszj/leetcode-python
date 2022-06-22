from typing import List

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

isBadVersion = None

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid) and (mid == 1 or not isBadVersion(mid - 1)):
                # 找到first bad
                return mid

            if isBadVersion(mid):
                # 往前走
                right = mid - 1
            else:
                left = mid + 1

    def setup(self, bad: int):
        global isBadVersion

        def isbad(version: int):
            return version >= bad

        isBadVersion = isbad
        return self


def test_solution():
    input1 = [(
        dict(n = 5, bad = 4), 4
    ),(
        dict(n = 1, bad = 1), 1
    )]

    for input, expect in input1:
        assert Solution().setup(input['bad']).firstBadVersion(input['n']) == expect, (input, expect)