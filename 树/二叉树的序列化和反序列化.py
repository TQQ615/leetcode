"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/serialize-and-deserialize-binary-tree

eg1:
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "None,"
        return str(root.val) + "," + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def deserialize_demo(data_list):
            if len(data_list) <= 0:
                return None
            val = data_list[0]
            data_list.pop(0)
            if val == "None":
                return None
            left = deserialize_demo(data_list)
            right = deserialize_demo(data_list)
            return TreeNode(val, left, right)

        data_list = data.split(",")[:-1]
        print('data_list: ', data_list)
        return deserialize_demo(data_list)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


if __name__ == '__main__':
    ser = Codec()
    deser = Codec()
    ll = TreeNode(2)
    rr = TreeNode(3, TreeNode(4), TreeNode(5))
    root = TreeNode(1, left=ll, right=rr)
    ans = deser.deserialize(ser.serialize(root))
    print(ans)