from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        # base case
        if len(nums) == 1:
            return [nums[:]]

        for _ in nums:
            num: int = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                result.append([*perm, num])
            # 这里是体现back tracking的时候
            nums.append(num)
        return result


def test_solution():
    examples = [
        ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
        ([0,1], [[0,1],[1,0]]),
        ([1], [[1]]),
    ]
    for input, expect in examples:
        res = Solution().permute(input)
        assert sorted(res) == sorted(expect), (input, expect, res)