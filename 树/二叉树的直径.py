"""EASY
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
eg1:给定二叉树
          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
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
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 回溯函数返回的结果始终是某侧子树的最大深度，只在内部判断最大直径
        def backtrace(root):
            if root is None:
                return 0
            left_max = backtrace(root.left)
            right_max = backtrace(root.right)
            demo = left_max + right_max
            if demo > self.diameter:
                self.diameter = demo
            return 1 + max(left_max, right_max)

        backtrace(root)
        return self.diameter


if __name__ == '__main__':
    solution = Solution()
    p1 = TreeNode(2, TreeNode(4), TreeNode(5))
    p2 = TreeNode(3)
    p = TreeNode(1, p1, p2)
    print(solution.diameterOfBinaryTree(p))
