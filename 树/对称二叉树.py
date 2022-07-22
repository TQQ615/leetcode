"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。

eg1:
输入：root = [1,2,2,3,4,4,3]
输出：true
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def backtrace(left, right):
            if left is None and right is None:
                return True
            if left is not None and right is not None:
                if left.val == right.val:
                    return backtrace(left.left, right.right) and backtrace(left.right, right.left)
            return False
        return backtrace(root.left, root.right)


if __name__ == '__main__':
    solution = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(2)
    t4 = TreeNode(3)
    t5 = TreeNode(4)
    t6 = TreeNode(4)
    t7 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    print(solution.isSymmetric(t1))
