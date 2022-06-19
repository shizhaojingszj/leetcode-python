class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # instructions只有三种char: GLR
        # 形成环的判断有：
        ## 1. 回到原点
        ## 2. 改了方向

        # 数据结构，以原点(0,0)为起始位置，North为(0,1)，[x,y]需要进行的修改。以顺时针排序。
        ## 由于是顺时针排序，所以L（转左）为-1
        ## R（转右）为+1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # 遍历instructions得到最终状态
        xy = (0, 0)
        # 初始为North
        direction_idx = 0
        for i in instructions:
            direction = directions[direction_idx]
            if i == "G":
                # 这时改变坐标
                xy = (
                    xy[0] + direction[0],  # x轴偏移量
                    xy[1] + direction[1],  # y轴偏移量
                )
            elif i == "L":
                # 这时改变direction_idx
                direction_idx = (direction_idx - 1) % 4
            elif i == "R":
                # 改变direction_idx
                direction_idx = (direction_idx + 1) % 4
            else:
                raise ValueError(i)

        return xy == (0, 0) or direction_idx != 0


def test_solution():
    input1 = [
        ("GGLLGG", True),
        ("GG", False),
        ("GL", True),
    ]

    for input, expect in input1:
        assert Solution().isRobotBounded(input) == expect, (input, expect)
