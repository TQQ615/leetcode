"""
给你两棵二叉树： root1 和 root2 。

想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。
你需要将这两棵树合并成一棵新二叉树。
合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，不为 null 的节点将直接作为新二叉树的节点。

返回合并后的二叉树。

注意: 合并过程必须从两个树的根节点开始。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/merge-two-binary-trees

eg1:
输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
输出：[3,4,5,5,4,null,7]

eg2:
输入：root1 = [1], root2 = [1,2]
输出：[2,2]
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def merge(tree1, tree2):
            tree = None
            if tree1 is not None and tree2 is not None:
                tree = TreeNode(tree1.val + tree2.val, merge(tree1.left, tree2.left), merge(tree1.right, tree2.right))
            elif tree1 is None:
                tree = tree2
            elif tree2 is None:
                tree = tree1
            return tree
        return merge(root1, root2)


if __name__ == '__main__':
    solution = Solution()
    t1 = TreeNode(1, TreeNode(3, TreeNode(5), None), TreeNode(2))
    t2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))

    def preOrder(root):
        if root is None:
            return
        print(root.val)
        preOrder(root.left)
        preOrder(root.right)

    preOrder(solution.mergeTrees(t1, t2))
