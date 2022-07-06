"""
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

eg1:
输入：root = [3,1,4,null,2], k = 1
输出：1

eg2:
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.rk = 0
        self.relt = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def backtrace(node):
            if node is None:
                return
            backtrace(node.left)
            self.rk += 1
            if self.rk == k:
                self.relt = node.val
                return
            backtrace(node.right)
        backtrace(root)
        return self.relt