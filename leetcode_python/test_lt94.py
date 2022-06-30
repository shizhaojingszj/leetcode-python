# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from .test_lt337 import TreeNode, Tree

from typing import Optional, List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.from_node(root)

    def from_node(self, node: Optional[TreeNode]) -> List[int]:
        if node is None:
            return []
        res: List[int] = []
        if node.left:
            res.extend(self.from_node(node.left))

        res.append(node.val)
        if node.right:
            res.extend(self.from_node(node.right))

        return res


def setup_tree(nodes):
    return Tree(nodes)


# TODO: class Tree is not good enough
# Leetcode online submit passed
def test_solution():
    input1 = [
        (dict(root = [1,None,2,3]), [1,3,2]),
        (dict(root = []), []),
        (dict(root = [1]), [1]),
    ]

    for input, expect in input1:
        tree = setup_tree(input['root'])
        assert Solution().inorderTraversal(tree.root) == expect, (input, expect)
