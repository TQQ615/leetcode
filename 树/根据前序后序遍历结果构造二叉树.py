"""
给定两个整数数组，preorder和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，
postorder 是同一棵树的后序遍历，重构并返回二叉树。

如果存在多个答案，您可以返回其中 任何 一个。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal

eg1:
输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]

"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        if len(preorder) <= 0 and len(postorder) <= 0:
            return None
        if len(preorder) == 1 and len(postorder) == 1:
            return TreeNode(preorder[0])
        root_val = preorder[0]
        left_val = preorder[1]
        idx = postorder.index(left_val)
        return TreeNode(
            root_val,
            self.constructFromPrePost(preorder[1: 2 + idx], postorder[:idx + 1]),
            self.constructFromPrePost(preorder[2 + idx:], postorder[idx + 1: -1])
        )