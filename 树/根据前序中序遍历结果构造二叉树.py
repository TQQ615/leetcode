"""
给定两个整数数组 preorder 和 inorder，其中preorder 是二叉树的先序遍历， inorder是同一棵树的中序遍历，请构造二叉树并返回其根节点。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal

eg1:
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]

"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) <= 0 and len(inorder) <= 0:
            return None
        root_val = preorder[0]
        idx = inorder.index(root_val)
        return TreeNode(root_val,
                        self.buildTree(preorder[1:idx + 1], inorder[:idx]),
                        self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
                        )