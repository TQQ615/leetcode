"""
给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，二叉树。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal

eg1:
输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]

"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) <= 0 and len(postorder) <= 0:
            return None
        root_val = postorder[-1]
        idx = inorder.index(root_val)
        return TreeNode(root_val,
                        self.buildTree(inorder[:idx], postorder[:idx]),
                        self.buildTree(inorder[idx + 1:], postorder[idx:-1])
                        )