class Solution:
    def convert(self, s: str, numRows: int) -> str:
        a = [[] for _ in range(numRows)]

        assert numRows >= 1
        if numRows == 1: return s
        A = numRows * 2 - 2
        # 就是这里找规律，纸上画一下
        def get_num_row(index: int) -> int:
            mod = index % A
            if mod <= numRows - 1:
                return mod
            else:
                return A - mod

        for i, char in enumerate(s):
            numRow = get_num_row(i)
            a[numRow].append(char)

        b = ["".join(row) for row in a]
        return "".join(b)
            


def test_solution():
    examples = [
        (("A", 1), "A"),
        (("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"),
        (("PAYPALISHIRING", 4), "PINALSIGYAHRPI"),
    ]
    for input, expect in examples:
        anw = Solution().convert(*input)
        assert anw == expect, (input, expect, anw)
