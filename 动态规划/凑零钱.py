"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回-1 。

你可以认为每种硬币的数量是无限的。
eg1:
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

eg2:
输入：coins = [2], amount = 3
输出：-1

eg3:
输入：coins = [1], amount = 0
输出：0

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/coin-change]
"""


# 动态规划：状态转移方程：f(n) = min_i(f(n - coin_i))
# 时间复杂度: O(2^n)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        relt = float("inf")
        for c in coins:
            pre_relt = self.coinChange(coins, amount - c)
            if pre_relt == -1:
                continue
            relt = min(relt, 1 + pre_relt)
        return relt if relt != float("inf") else -1


# 时间复杂度: O(n)
class Solution2(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        relt = [-1] * (amount + 1)
        relt[0] = 0
        for i in range(1, amount + 1):
            final = float("inf")
            for c in coins:
                if i >= c:
                    pre_relt = relt[i - c]
                    if pre_relt == -1:
                        continue
                    final = min(final, 1 + pre_relt)
            relt[i] = final if final != float("inf") else -1
        return relt[amount]


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange([1, 2, 5], 11))
    print(solution.coinChange([2], 3))
    print(solution.coinChange([1], 0))
