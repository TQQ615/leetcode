"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：
“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree

eg1:
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

eg2:
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

eg3:
输入：root = [1,2], p = 1, q = 2
输出：1
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # TODO: 指定的节点p和q一定存在于树中
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def find(root, val1, val2):
            if root is None:
                return None
            if root.val == val1 or root.val == val2:
                return root
            left = find(root.left, val1, val2)
            right = find(root.right, val1, val2)
            if left is not None and right is not None:
                return root
            return left if left is not None else right

        return find(root, p.val, q.val)


"""
给定一棵二叉树的根节点 root，返回给定节点 p 和 q 的最近公共祖先（LCA）节点。
如果 p 或 q 之一 不存在 于该二叉树中，返回 null。树中的每个节点值都是互不相同的。

根据维基百科中对最近公共祖先节点的定义：
“两个节点 p 和 q 在二叉树 T 中的最近公共祖先节点是 后代节点 中既包括 p又包括q的最深节点（我们允许 一个节点为自身的一个后代节点 ）”。
一个节点 x的 后代节点 是节点x 到某一叶节点间的路径中的节点 y。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-ii

eg1:
输入： root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
输出： null
解释： 节点 10 不存在于树中，所以返回 null。

"""


class Solution2:
    def __init__(self, find_p=False, find_q=False):
        self.find_p = find_p
        self.find_q = find_q

    # TODO: p和q不一定在数中
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> None:

        def lca(root, p, q):
            if root is None:
                return None

            left = lca(root.left, p, q)
            right = lca(root.right, p, q)
            # 后序的关系，否则类似（5，4），找到5就直接返回了，不会再遍历4，就认为4找不到
            if root.val == p.val:
                self.find_p = True
                return root
            if root.val == q.val:
                self.find_q = True
                return root

            if left is not None and right is not None:
                return root
            return left if left is not None else right

        res = lca(root, p, q)
        if self.find_p and self.find_q:
            return res
        return None


"""
给定一棵二叉树中的两个节点 p 和 q，返回它们的最近公共祖先节点（LCA）。

每个节点都包含其父节点的引用（指针）。Node的定义如下：

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution3:
    # TODO: 指定的节点p和q一定存在于树中
    #  你就把二叉树节点当成链表节点，parent 指针就是链表节点的 next 指针，最近公共祖先就是两个链表的交点，这道题就解决了。
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a = p
        b = q
        while a != b:
            if a is None:
                a = q
            else:
                a = a.parent
            if b is None:
                b = p
            else:
                b = b.parent
        return a


"""
给定一棵二叉树的根节点root和TreeNode类对象的数组（列表）nodes，返回nodes中所有节点的最近公共祖先（LCA）。
数组（列表）中所有节点都存在于该二叉树中，且二叉树中所有节点的值都是互不相同的。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

eg1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
输出: 2
解释:节点 4 和 7 的最近公共祖先是 2。

eg2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
输出: 5
解释:节点 7、6、2 和 4 的最近公共祖先节点是 5。

"""


class Solution4:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        target_val = [x.val for x in nodes]

        def lca(root):
            if root is None:
                return None

            left = lca(root.left)
            right = lca(root.right)

            if root.val in target_val:
                return root
            if left is not None and right is not None:
                return root
            return left if left is not None else right

        return lca(root)


if __name__ == '__main__':
    solution = Solution()
    solution2 = Solution2()
    solution3 = Solution3()
    solution4 = Solution4()
    t31 = TreeNode(7)
    t32 = TreeNode(4)
    t21 = TreeNode(6)
    t22 = TreeNode(2, t31, t32)
    t11 = TreeNode(5, t21, t22)
    t23 = TreeNode(0)
    t24 = TreeNode(8)
    t12 = TreeNode(1, t23, t24)
    t = TreeNode(3, t11, t12)
    print(solution.lowestCommonAncestor(t, t11, t12).val)
    x = solution2.lowestCommonAncestor(t, t11, TreeNode(4))
    print(x.val if x is not None else 'None')

    n31 = Node(7)
    n32 = Node(4)
    n21 = Node(6)
    n22 = Node(2)
    n23 = Node(0)
    n24 = Node(8)
    n11 = Node(5)
    n12 = Node(1)
    n = Node(3)
    n31.parent = n22
    n32.parent = n22
    n22.left = n31
    n22.right = n32
    n11.left = n21
    n11.right = n22
    n22.parent = n11
    n21.parent = n11
    n12.left = n23
    n12.right = n24
    n23.parent = n12
    n24.parent = n12
    n.left = n11
    n.right = n12
    n11.parent = n
    n12.parent = n
    print(solution3.lowestCommonAncestor(n11, n12).val)

    print(solution4.lowestCommonAncestor(t, [t21, t22, t31, t32]).val)




