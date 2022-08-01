"""
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的key对应的节点，并保证二叉搜索树的性质不变。
返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/delete-node-in-a-bst

eg1:
输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
另一个正确答案是 [5,2,6,null,4,null,7]。

eg2:
输入: root = [5,3,6,2,4,null,7], key = 0
输出: [5,3,6,2,4,null,7]
解释: 二叉树不包含值为 0 的节点
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def getMin(root):
            while root.left is not None:
                root = root.left
            return root

        def bfs(root, val):
            if root is None:
                return None
            # root.val 比要找的值小，则从他的右子树找
            if root.val < val:
                root.right = bfs(root.right, val)
            # root.val 比要找的值大，则从他的左子树找
            if root.val > val:
                root.left = bfs(root.left, val)
            # 找到该值，直接删除
            if root.val == val:
                # 如果有一侧是None，直接返回另一侧
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left
                # 用右侧最小值代替当前节点（也可用左侧最大值代替）
                # 先找到右侧最小点
                minNode = getMin(root.right)
                # 交换值
                root.val = minNode.val
                # 删掉右子树中最小点：递归使用本方法
                root.right = bfs(root.right, minNode.val)
            return root
        return bfs(root, key)


def printRootMid(root):
    if root is None:
        # print('null')
        return
    printRootMid(root.left)
    print(root.val)
    printRootMid(root.right)


if __name__ == '__main__':
    solution = Solution()
    t = TreeNode(5,
                 TreeNode(3, TreeNode(2), TreeNode(4)),
                 TreeNode(6, None, TreeNode(7))
                 )
    tt = solution.deleteNode(t, 3)
    printRootMid(tt)
