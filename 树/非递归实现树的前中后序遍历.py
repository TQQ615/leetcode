class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
前序
"""


# 递归实现
def front_r(root):
    if root is None:
        return
    print(root.val)
    front_r(root.left)
    front_r(root.right)


# 非递归实现
def front(root):
    if root is None:
        return
    stack = []
    node = root
    while len(stack) > 0 or node is not None:
        while node is not None:
            print(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right


"""
中序
"""


def mid_r(root):
    if root is None:
        return
    mid_r(root.left)
    print(root.val)
    mid_r(root.right)


def mid(root):
    if root is None:
        return
    stack = []
    node = root
    while len(stack) > 0 or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print(node.val)
        node = node.right


"""
后序
"""


def behind_r(root):
    if root is None:
        return
    behind_r(root.left)
    behind_r(root.right)
    print(root.val)


def behind(root):
    if root is None:
        return
    stack1 = [root]
    stack2 = []
    # 按照左右的顺序压入栈1，再将根压入栈2，逐个pop栈1中元素（先右再左）,重复这个过程，在栈2中拥有后序遍历的顺序
    while len(stack1) > 0:
        node = stack1.pop()
        if node.left is not None:
            stack1.append(node.left)
        if node.right is not None:
            stack1.append(node.right)
        stack2.append(node)
    while len(stack2) > 0:
        print(stack2.pop().val)


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
# front_r(root)
# front(root)
# mid_r(root)
# mid(root)
# behind_r(root)
behind(root)
