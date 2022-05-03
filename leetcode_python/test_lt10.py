class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        要点：
        1. 如何处理*
        2. 使用（i,j）两个下标作为要记录的点
        3. 可以使用cache，对helper函数进行处理

        下面是Top-Down的解法
        """
        cache = {}

        def dfs(i: int, j: int) -> bool:
            if (i, j) in cache:
                return cache[(i, j)]
            # 什么时候结束
            # 1. 当i和j同时out-of-bounds，则是perfect match
            if i >= len(s) and j >= len(p):
                return True
            # 2. 如果只有j是out-of-bounds，那么则没有match
            # e.g. abc ab
            if j >= len(p):
                return False

            # 3. 如果i是比out-of-bounds还要再多一个位置，那么就没有match
            if i > len(s):
                return False

            # 定义match：当前i，j是否有match；前提是i的index在里面
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # 考虑'*'
            if (j + 1 < len(p)) and p[j + 1] == "*":
                cache[(i, j)] = (
                    # a. 第一种可能性，使用"*"，但是此时必须match
                    (match and i + 1 <= len(s) and dfs(i + 1, j))
                    or
                    # b. 第二种可能性，不使用"*"，此时match不重要
                    dfs(i, j + 2)
                )
                return cache[(i, j)]

            cache[(i, j)] = match and dfs(i + 1, j + 1)
            return cache[(i, j)]

        return dfs(0, 0)


def test_solution():
    examples = [
        (("a", ".*.."), False),
        (("aaa", ".*"), True),
        (("aa", "a"), False),
        (("aa", "a*"), True),
        (("ab", ".*"), True),
        (("aab", "a*b"), True),
        (("aab", "c*a*b*"), True),
    ]
    for input, expect in examples:
        anw = Solution().isMatch(*input)
        assert anw == expect, (input, expect, anw)
