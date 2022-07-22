"""
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

eg1:
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        relt = []
        stack = [[root]]
        if root is None:
            return relt
        while len(stack) > 0:
            node_list = stack.pop(0)
            val_list = []
            node_ll = []
            for node in node_list:
                val_list.append(node.val)
                if node.left is not None:
                    node_ll.append(node.left)
                if node.right is not None:
                    node_ll.append(node.right)
            relt.append(val_list)
            if len(node_ll) > 0:
                stack.append(node_ll)
        return relt


if __name__ == '__main__':
    solution = Solution()
    t1 = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5
    print(solution.levelOrder(t1))