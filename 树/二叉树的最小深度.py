""" EASY
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

eg1:
输入：root = [3,9,20,null,null,15,7]
输出：2

eg2:
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS 广度优先遍历
# BFS 可以找到最短距离；
# 但是空间复杂度高: 队列中每次都会储存着二叉树一层的节点，这样的 话最坏情况下空间复杂度应该是树的最底层节点的数量，也就是 N/2 ，也就是 O(N) 。
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        tree_list = list()
        tree_list.append((root, 1))
        while len(tree_list) > 0:
            p, deepth = tree_list[0]
            tree_list.remove((p, deepth))
            if p.left is None and p.right is None:
                return deepth
            if p.left is not None:
                tree_list.append((p.left, deepth + 1))
            if p.right is not None:
                tree_list.append((p.right, deepth + 1))


# DFS 深度优先遍历
# 空间复杂度无非就是递归堆栈，最坏情况下顶多就是树的高度，也就是 O(logN)
class Solution2(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        mindeepth = 10**9
        if root.left:
            mindeepth = min(mindeepth, self.minDepth(root.left) + 1)
        if root.right:
            mindeepth = min(mindeepth, self.minDepth(root.right) + 1)
        return mindeepth


if __name__ == '__main__':
    solution = Solution2()
    p1 = TreeNode(9)
    p2 = TreeNode(20, TreeNode(15), TreeNode(7))
    p = TreeNode(3, p1, p2)
    print(solution.minDepth(p))
