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

    def permute1(self, nums: List[int]) -> List[List[int]]:
        result = []

        def recursive(nums):
            # base case
            if len(nums) == 1:
                return [ nums[:] ]

            res = []
            
            N2 = len(nums)
            for n in range(N2):
                # 每次先pop出来最前面的值
                num = nums.pop(0)
                perms = recursive(nums)
                for perm in perms:
                    perm.append(num)
                res.extend([x[:] for x in perms])
                # 再放回去到最后一个位置
                nums.append(num)
            return res

        # 这里必须返回的是最后一级
        result = recursive(nums)

        return result



def test_solution():
    examples = [
        ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
        ([0,1], [[0,1],[1,0]]),
        ([1], [[1]]),
    ]
    for input, expect in examples:
        res = Solution().permute1(input)
        assert set(map(tuple, res)) == set(map(tuple, expect)), (input, expect, res)