"""
就是用set + slidingWindow（two pointers）
1. 用dict记录之前见过的char的位置
2. 在出现重复char之后，要从dict中去掉这个char“之前”到i为止的那些char
"""


class Solution1:
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


def test_solution1():
    examples = [
        ("tmmzuxt", 5),
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ]

    for input, expect in examples:
        res = Solution1().lengthOfLongestSubstring(input)
        assert expect == res, (input, expect, res)


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        N = len(s)
        d = {}
        max_length = 0

        while left < N and right < N:
            # 一次只看right位置上的char
            char = s[right]
            if char not in d:
                # 记录char最后出现的位置
                d[char] = right
            else:
                left = max(left, d[char] + 1)
                d[char] = right

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length


def test_solution2():
    examples = [
        ("tmmzuxt", 5),
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ]

    for input, expect in examples:
        res = Solution2().lengthOfLongestSubstring(input)
        assert expect == res, (input, expect, res)
