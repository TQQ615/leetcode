"""
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：

节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/convert-bst-to-greater-tree

eg1:
输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

eg2:
输入：root = [1,0,2]
输出：[3,3,2]

eg3:
输入：root = [3,2,4,1]
输出：[7,9,4,10]
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
        self.sum_ = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def traceback(root):
            if root is None:
                return
            traceback(root.right)
            self.sum_ += root.val
            root.val = self.sum_
            traceback(root.left)

        traceback(root)
        return root


def printRootMid(root):
    if root is None:
        return
    printRootMid(root.left)
    print(root.val)
    printRootMid(root.right)


if __name__ == '__main__':
    solution = Solution()
    t = TreeNode(4,
                 TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))),
                 TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8)))
                 )
    tt = solution.convertBST(t)
    printRootMid(tt)
