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


if __name__ == '__main__':
    solution = Solution()
    print(solution.numTrees(3))
