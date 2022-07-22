"""
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-tree-maximum-path-sum

eg1:
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
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
        self.relt = 0

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def backtrace(node):
            if node is None:
                return 0
            leftmaxpath = max(backtrace(node.left), 0)
            rightmaxpath = max(backtrace(node.right), 0)

            pathsum = node.val + leftmaxpath + rightmaxpath
            if pathsum > self.relt:
                self.relt = pathsum

            print('node.val: ', node.val, "left: ", leftmaxpath, "right: ", rightmaxpath, "relt: ", self.relt)
            return max(leftmaxpath, rightmaxpath) + node.val

        x = backtrace(root)
        return self.relt


if __name__ == '__main__':
    solution = Solution()
    # t1 = TreeNode(-10)
    # t2 = TreeNode(9)
    # t3 = TreeNode(20)
    # t4 = TreeNode(15)
    # t5 = TreeNode(7)
    # t1.left = t2
    # t1.right = t3
    # t3.left = t4
    # t3.right = t5

    # t1 = TreeNode(2, TreeNode(-1))
    t1 = TreeNode(2, TreeNode(-1), TreeNode(-2))
    # [2, -1, -2]
    print(solution.maxPathSum(t1))
