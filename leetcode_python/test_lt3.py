"""
就是用set + slidingWindow（two pointers）
1. 用dict记录之前见过的char的位置
2. 在出现重复char之后，要从dict中去掉这个char“之前”到i为止的那些char
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = dict()
        length = 0
        # 起点是最左端
        i = 0
        if len(s) == 1:
            return 1
        j = 0
        while j < len(s):
            c = s[j]
            if c not in cache:
                # 需要记录之前见到的这个char的位置
                cache[c] = j
                # 前指针向右走
                j += 1
                length = max(j - i, length)
            else:
                # 要去掉重复c之前的那些char
                for ii in range(i, cache[c]):
                    cache.pop(s[ii])
                # i要跳过这个char
                i = cache[c] + 1
                # 记录位置仍然是重要的
                cache[c] = j
                j += 1
        return length


def test_solution():
    examples = [
        ("tmmzuxt", 5),
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ]

    for input, expect in examples:
        res = Solution().lengthOfLongestSubstring(input)
        assert expect == res, (input, expect, res)
