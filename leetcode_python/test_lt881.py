from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        N = len(people)

        # result
        number = 0

        left = 0
        right = N - 1

        while left < right:
            # 尝试一船装两个
            if people[left] + people[right] <= limit:
                number += 1
                left += 1
                right -= 1
            # 只能装大的
            else:
                number += 1
                right -= 1

        # 剩一个的情况
        if left == right:
            number += 1

        return number


def test_solution():
    input1 = [(
        dict(people = [1,2], limit = 3),
        1,
    ), (
        dict(people = [3,2,2,1], limit = 3),
        3,
    )]

    for input, expect in input1:
        assert Solution().numRescueBoats(**input) == expect, (input, expect)