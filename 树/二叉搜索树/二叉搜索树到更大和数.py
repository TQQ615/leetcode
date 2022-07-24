"""
给定一个二叉搜索树root(BST)，请将它的每个节点的值替换成树中大于或者等于该节点值的所有节点值之和。

提醒一下， 二叉搜索树 满足下列约束条件：

节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree

eg1:
输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

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
        self.sum_num = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def backtrace(node):
            if node is None:
                return
            backtrace(node.right)
            self.sum_num += node.val
            node.val = self.sum_num
            backtrace(node.left)
            return node
        return backtrace(root)