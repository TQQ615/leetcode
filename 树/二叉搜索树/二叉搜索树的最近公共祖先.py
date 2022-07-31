"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树: root =[6,2,8,0,4,7,9,null,null,3,5]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree

eg1:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。

eg2:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        max_val = max(p.val, q.val)
        min_val = min(p.val, q.val)

        def lca(root):
            if root is None:
                return None
            if root.val > max_val:
                return lca(root.left)

            if root.val < min_val:
                return lca(root.right)

            return root

        return lca(root)


if __name__ == '__main__':
    solution = Solution()
    t31 = TreeNode(3)
    t32 = TreeNode(5)
    t21 = TreeNode(0)
    t22 = TreeNode(4, t31, t32)
    t11 = TreeNode(2, t21, t22)
    t23 = TreeNode(7)
    t24 = TreeNode(9)
    t12 = TreeNode(8, t23, t24)
    t = TreeNode(6, t11, t12)
    print(solution.lowestCommonAncestor(t, t11, t22).val)