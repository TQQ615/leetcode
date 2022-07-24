"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/validate-binary-search-tree

eg1:
输入：root = [2,1,3]
输出：true

eg2:
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 中序遍历实现
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return []
            return dfs(root.left) + [root.val] + dfs(root.right)

        ll = dfs(root)
        for i in range(1, len(ll)):
            if ll[i] < ll[i - 1]:
                return False
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # max_ 节点node需要对比的最大值
        # min_ 节点node需要对比的最小值
        def getTree(node, max_, min_):
            if node is None:
                return True
            if max_ is not None and max_.val <= node.val:
                return False
            if min_ is not None and min_.val >= node.val:
                return False
            # 对于左子树node.left来说，需要对比的最大值是当前节点node,最小值是上一步保留的最小值
            # 对于右子树node.right来说，需要对比的最大值当前节点上一步保留的最大值，最小值是当前节点node
            return getTree(node.left, node, min_) and getTree(node.right, max_, node)

        return getTree(root, None, None)


if __name__ == '__main__':
    solution = Solution()
    t1 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(solution.isValidBST(t1))
