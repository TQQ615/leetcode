"""
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组nums中。

现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。
这里的 i - 1 和 i + 1 代表和i相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

求所能获得硬币的最大数量。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/burst-balloons

eg1:
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

eg2:
输入：nums = [1,5]
输出：10
"""
from typing import Optional, List


class Solution:
    def __init__(self):
        self.relt = 0
        self.max_relt = 0

    # 全排列 回溯
    def maxCoins1(self, nums: List[int]) -> int:

        def backtrace(ll):
            if len(ll) == 0:
                self.max_relt = max(self.max_relt, self.relt)
                return
            for i in range(len(ll)):
                left = ll[i - 1] if i - 1 >= 0 else 1
                right = ll[i + 1] if i + 1 < len(ll) else 1
                self.relt += left * ll[i] * right
                backtrace(ll[:i] + ll[i + 1:])
                self.relt -= left * ll[i] * right
        backtrace(nums)
        return self.max_relt

    # 动态规划：
    def maxCoins(self, nums: List[int]) -> int:
        points = [1] + nums + [1]
        n = len(nums)
        # dp状态矩阵：dp[i][j]表示：戳破第i个气球到第j个气球之间的气球（开区间），最大收益是多少
        # 最后求dp[0][n + 1]
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

        for l in range(1, n + 2):
            for i in range(n + 2 - l):
                j = i + l
                for k in range(i + 1, j):
                    # 状态转移：(i, j)之间的最大收益 = 最后留下的元素k * 左边 * 右边 中最大的收益
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k] + dp[k][j] + points[i] * points[k] * points[j])
        return dp[0][n + 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxCoins(nums = [3,1,5,8]))
    print(solution.maxCoins(nums = [1,5]))


