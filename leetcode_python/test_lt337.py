from typing import Optional, List, Any


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, all_nodes: List[Optional[Any]]):
        self.vals = all_nodes
        self.root = None
        # self.root = self.to_node(0)
        self.root = None
        # this is list
        level_nodes = []
        # next level nodes
        new_level_nodes = []
        # 在all_nodes中的index
        i = 0
        while True:
            if i == 0:
                # 获取root的val
                val = all_nodes[i]
                i += 1
                # 修改self.root
                self.root = TreeNode(val)
                # 记录第一层二叉树层里面的所有node
                level_nodes.append(self.root)
                continue
            # 判断level_nodes的大小跟level的关系
            for node in level_nodes:
                # 获取下一对left和right
                if i >= len(all_nodes):
                    return
                left_right = all_nodes[i:(i+2)]
                if len(left_right) == 2:
                    lv, rv = left_right
                else:
                    lv = left_right
                    rv = None
                i += 2
                node.left = TreeNode(lv) if lv is not None else None
                node.right = TreeNode(rv) if rv is not None else None
                for child in [node.left, node.right]:
                    if child:
                        new_level_nodes.append(child)
            level_nodes = new_level_nodes


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))

    def dfs(self, node: TreeNode) -> List[int]:
        if node is None:
            # rob, not_rob
            return [0, 0]
        
        # node被rob时
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        rob = node.val + left[1] + right[1]
        # node不被rob时
        not_rob = max(left) + max(right)

        return [rob, not_rob]


def test_solution():
    input1 = [
        (
            dict(root=[3, 2, 3, None, 3, None, 1]),
            7,
        ),
        (
            dict(root=[3, 4, 5, 1, 3, None, 1]),
            9,
        ),
        # Time limit
        (
            dict(root=[79,99,77,None,None,None,69,None,60,53,None,73,11,None,None,None,62,27,62,None,None,98,50,None,None,90,48,82,None,None,None,55,64,None,None,73,56,6,47,None,93,None,None,75,44,30,82,None,None,None,None,None,None,57,36,89,42,None,None,76,10,None,None,None,None,None,32,4,18,None,None,1,7,None,None,42,64,None,None,39,76,None,None,6,None,66,8,96,91,38,38,None,None,None,None,74,42,None,None,None,10,40,5,None,None,None,None,28,8,24,47,None,None,None,17,36,50,19,63,33,89,None,None,None,None,None,None,None,None,94,72,None,None,79,25,None,None,51,None,70,84,43,None,64,35,None,None,None,None,40,78,None,None,35,42,98,96,None,None,82,26,None,None,None,None,48,91,None,None,35,93,86,42,None,None,None,None,0,61,None,None,67,None,53,48,None,None,82,30,None,97,None,None,None,1,None,None]),
            3038,
        )
    ]

    for input, expect in input1:
        assert Solution().rob(Tree(input['root']).root) == expect, (input, expect)
