"""
给定二叉搜索树（BST）的根节点root和要插入树中的值value，将值插入二叉搜索树。
返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。

注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/insert-into-a-binary-search-tree

eg1:
输入：root = [4,2,7,1,3], val = 5
输出：[4,2,7,1,3,5]

eg2:
输入：root = [40,20,60,10,30,50,70], val = 25
输出：[40,20,60,10,30,50,70,null,null,25]

eg3:
输入：root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
输出：[4,2,7,1,3,5]
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def bfs(root, val):
            if root is None:
                return TreeNode(val)
            if root.val > val:
                root.left = bfs(root.left, val)
            if root.val < val:
                root.right = bfs(root.right, val)
            return root
        return bfs(root, val)


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
    tt = solution.insertIntoBST(t, 5)
    printRootMid(tt)
