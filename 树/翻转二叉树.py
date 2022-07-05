"""
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
eg1:
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

eg2:
输入：root = [2,1,3]
输出：[2,3,1]
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        return root


if __name__ == '__main__':
    solution = Solution()
    p1 = TreeNode(2, TreeNode(1), TreeNode(3))
    p2 = TreeNode(7, TreeNode(6), TreeNode(9))
    p = TreeNode(4, p1, p2)
    print(solution.invertTree(p))
