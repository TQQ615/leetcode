"""
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

eg1:
输入：n = 3
输出：5

eg2:
输入：n = 1
输出：1
"""
from typing import Optional, List


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            # 每个点i为根节点的时候
            # 递归左边包含j 个节点，右边包含 i - 1 - j个节点，
            # 左边的不同树的种类*右边不同树的种类，就是当前节点的种类之和
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]


"""
给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。

eg1:
输入：n = 3
输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

eg2:
输入：n = 1
输出：[[1]]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/unique-binary-search-trees-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution2:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def buildTree(start, end):
            if start > end:
                return [None]
            relt = []
            for i in range(start, end + 1):
                left = buildTree(start, i - 1)
                right = buildTree(i + 1, end)
                for p in left:
                    for q in right:
                        root = TreeNode(i)
                        root.left = p
                        root.right = q
                        relt.append(root)
            return relt
        return buildTree(1, n)


def printRootMid(root):
    if root is None:
        # print('null')
        return
    printRootMid(root.left)
    print(root.val)
    printRootMid(root.right)


if __name__ == '__main__':
    # solution = Solution()
    # print(solution.numTrees(3))

    solution = Solution2()
    relt = solution.generateTrees(3)
    print(len(relt))
    for i in range(len(relt)):
        print('第 %s 棵树: ' % i)
        printRootMid(relt[i])
