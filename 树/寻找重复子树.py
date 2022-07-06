"""
给定一棵二叉树 root，返回所有重复的子树。

对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

如果两棵树具有相同的结构和相同的结点值，则它们是重复的。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-duplicate-subtrees

eg1:
输入：root = [1,2,3,4,null,2,4,null,null,4]
输出：[[2,4],[4]]
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        relt = list()
        dic = dict()

        def backtrace(node):
            if node is None:
                return "None"
            left = backtrace(node.left)
            right = backtrace(node.right)

            ss = left + "," + right + "," + str(node.val)
            ll = dic.get(ss, 0)
            if ll == 1:
                relt.append(node)
            dic.update({ss: ll + 1})
            return ss

        backtrace(root)
        return relt
