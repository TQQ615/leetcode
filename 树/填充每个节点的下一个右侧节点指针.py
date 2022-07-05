"""
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有next 指针都被设置为 NULL。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/populating-next-right-pointers-in-each-node

eg1:
输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，
如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。
"""

from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# 时间复杂度，需要优化
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # 两个子树之间无法连接 ！！！
        # if root is None:
        #     return
        # root.left.next = root.right
        # root.right.next = None
        #
        # self.connect(root.left)
        # self.connect(root.right)
        # return root
        def backtrace(tree1, tree2):
            if tree1 is None or tree2 is None:
                return
            tree1.next = tree2

            backtrace(tree1.left, tree1.right)
            backtrace(tree2.left, tree2.right)
            backtrace(tree1.right, tree2.left)

        if root is None:
            return root
        backtrace(root.left, root.right)
        return root


# 逐层向下
class Solution2:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        leftmost = root

        while leftmost.left:
             head = leftmost
             while head:
                 head.left.next = head.right
                 if head.next:
                     head.right.next = head.next.left
                 head = head.next
             leftmost = leftmost.left
        return root


if __name__ == '__main__':
    solution = Solution2()
    p1 = Node(2, Node(4), Node(5))
    p2 = Node(3, Node(6), Node(7))
    p = Node(1, p1, p2)
    print(solution.connect(p))