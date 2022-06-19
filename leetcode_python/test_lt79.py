from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 从每一个位置开始，进行dfs
        rowN = len(board)
        colN = len(board[0])

        for i in range(rowN):
            for j in range(colN):
                if self.dfs(board, rowN, colN, i, j, word, 0):
                    return True

        return False

    def dfs(self, board, rowN, colN, i, j, word, index: int):
        # base
        ## 当ij决定的位置不等于当前word[index]时：
        if i < 0 or i >= rowN or j < 0 or j >= colN or board[i][j] != word[index]:
            return False
        ## 找到的情况
        if index == len(word) - 1:
            return True

        # recursive
        ## backtracking要求
        board[i][j] = '\0'

        ## dfs核心逻辑
        found = (
            self.dfs(board, rowN, colN, i - 1, j, word, index + 1)
            or self.dfs(board, rowN, colN, i + 1, j, word, index + 1)
            or self.dfs(board, rowN, colN, i, j + 1, word, index + 1)
            or self.dfs(board, rowN, colN, i, j - 1, word, index + 1)
        )

        ## backtracking
        board[i][j] = word[index]

        return found

    def debug(self, board):
        res = []
        for row in board:
            res .append(" ".join(row))
        return "\n".join(res)


def test_solution():
    input1 = [
        (
            (
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "ABCCED",
            ),
            True,
        ),
        (
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"),
            True,
        ),
        (
            (
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "ABCB",
            ),
            False,
        ),
    ]
    for (board, word), expect in input1:
        assert Solution().exist(board, word) == expect, (Solution().debug(board), word, expect)
