"""
给定一个二叉树的根节点 root，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/path-sum-iii

eg1:
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。

eg2:
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3
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
        self.path_sum = 0
        self.target_dict = dict({0: 1})
        self.relt = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def bfs(root):
            if root is None:
                return

            self.path_sum += root.val
            # 从二叉树的根节点开始，路径和为 pathSum - targetSum 的路径条数
            # 就是路径和为 targetSum 的路径条数
            self.relt += self.target_dict.get(self.path_sum - targetSum, 0)
            # 记录从二叉树的根节点开始，路径和为 pathSum 的路径条数
            self.target_dict[self.path_sum] = self.target_dict.get(self.path_sum, 0) + 1

            bfs(root.left)
            bfs(root.right)

            self.target_dict[self.path_sum] = self.target_dict.get(self.path_sum, 0) - 1
            self.path_sum -= root.val

        bfs(root)
        return self.relt


if __name__ == '__main__':
    solution = Solution()
    t = TreeNode(10,
                 TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))),
                 TreeNode(-3, None, TreeNode(11))
                 )
    print(solution.pathSum(t, 8))


