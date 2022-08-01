"""
给定二叉搜索树（BST）的根节点root和一个整数值val。

你需要在 BST 中找到节点值等于val的节点。 返回以该节点为根的子树。 如果节点不存在，则返回null。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-in-a-binary-search-tree

eg1:
输入：root = [4,2,7,1,3], val = 2
输出：[2,1,3]

eg2:
输入：root = [4,2,7,1,3], val = 5
输出：[]
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def bfs(root):
            if root is None:
                return None
            if root.val > val:
                return bfs(root.left)
            if root.val < val:
                return bfs(root.right)
            if root.val == val:
                return root
        return bfs(root)


def printRootMid(root):
    if root is None:
        # print('null')
        return
    printRootMid(root.left)
    print(root.val)
    printRootMid(root.right)


if __name__ == '__main__':
    solution = Solution()
    t = TreeNode(4,
                 TreeNode(2, TreeNode(1), TreeNode(3)),
                 TreeNode(7)
                 )
    tt = solution.searchBST(t, 2)
    printRootMid(tt)
