"""EASY
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

eg1:
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS 广度优先遍历
# BFS 可以找到最短距离；
# 但是空间复杂度高: 队列中每次都会储存着二叉树一层的节点，这样的话最坏情况下空间复杂度应该是树的最底层节点的数量，也就是 N/2 ，也就是 O(N) 。
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth = 0
        if root is None:
            return 0
        trees = list()
        trees.append((root, 1))
        while len(trees) > 0:
            demo, depth = trees[0]
            trees.pop(0)
            if demo.left is None and demo.right is None:
                maxdepth = max(maxdepth, depth)
            if demo.left is not None:
                trees.append((demo.left, depth + 1))
            if demo.right is not None:
                trees.append((demo.right, depth + 1))
        return maxdepth


# DFS 深度优先遍历
# 空间复杂度无非就是递归堆栈，最坏情况下顶多就是树的高度，也就是 O(logN)
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left) + 1
        right_depth = self.maxDepth(root.right) + 1
        return max(left_depth, right_depth)


if __name__ == '__main__':
    solution = Solution()
    p1 = TreeNode(9)
    p2 = TreeNode(20, TreeNode(15), TreeNode(7))
    p = TreeNode(3, p1, p2)
    print(solution.maxDepth(p))

    solution2 = Solution2()
    print(solution2.maxDepth(p))
