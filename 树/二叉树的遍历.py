"""
前序位置的代码只能从函数参数中获取父节点传递来的数据，而后序位置的代码不仅可以获取参数数据，还可以获取到子树通过函数返回值传递回来的数据。
"""

"""
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
eg1:
输入：root = [1,null,2,3]
输出：[1,2,3]
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


if __name__ == '__main__':
    solution = Solution()
    p1 = TreeNode(9)
    p2 = TreeNode(2, TreeNode(3), None)
    p = TreeNode(1, None, p2)
    print(solution.preorderTraversal(p))
