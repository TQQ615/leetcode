"""EASY->HARD
大框架：

说明：
比如说 dp[3][2][1] 的含义就是:今天是第三天，我现在手上持有着股票，至今最多进行 2 次交易。
再比如 dp[2][3][0] 的含义:今天是第二天，我现在手上没有持有股 票，至今最多进行 3 次交易。

base case:
dp[-1][k][0] = dp[i][0][0] = 0 dp[-1][k][1] = dp[i][0][1] = -infinity
dp[-1][k][0] = 0
解释:因为 i 是从 0 开始的，所以 i = -1 意味着还没有开始，这时候的利润当然是 0 。
dp[-1][k][1] = -infinity 解释:还没开始的时候，是不可能持有股票的，用负无穷表示这种不可能。
dp[i][0][0] = 0
解释:因为 k 是从 1 开始的，所以 k = 0 意味着根本不允许交易，这时候利润当然是 0 。
dp[i][0][1] = -infinity 解释:不允许交易的情况下，是不可能持有股票的，用负无穷表示这种不可能。

状态转移方程:
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
"""

"""EASY: k=1
给定一个数组 prices ，它的第i 个元素prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock

eg1:
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

eg2:
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
"""


# EASY: k=1
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp_i_0 = 0
        dp_i_1 = -prices[0]
        for i in range(1, len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            # 注意：k=1，只买卖一次，所以所有的买都只消耗当天的价格
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0


# EASY: k= +infinity 可以购买无限次
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp_i_0 = 0
        dp_i_1 = -prices[0]
        for i in range(1, len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0

"""
给定一个整数数组prices，其中第prices[i]表示第i天的股票价格 。

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

作者：力扣 (LeetCode)
链接：https://leetcode.cn/leetbook/read/top-interview-questions-hard/xddkum/

eg1:
输入: prices = [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

eg2:
输入: prices = [1]
输出: 0
"""


# k = +infinity with cooldown 无限次购买，但是卖出之后第二天无法买入（冷冻期一天）
class Solution3(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 冷冻期只有1天可以用额外的变量代替，如果冷冻期更长，可以使用数组记录
        dp_pre_0 = 0
        dp_i_0 = 0
        dp_i_1 = -prices[0]
        for i in range(1, len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp
        return dp_i_0


# k = +infinity with fee
class Solution4(object):
    def maxProfit(self, prices, free):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp_i_0 = 0
        dp_i_1 = -prices[0]
        for i in range(1, len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i] - free)
        return dp_i_0


# k = 2
class Solution5(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp_i_k_0 = 0
        dp_i_k_1 = float("-inf")
        dp_i_kp1_0 = float("-inf")
        dp_i_kp1_1 = -prices[0]
        for i in range(1, len(prices)):
            dp_i_k_0 = max(dp_i_k_0, dp_i_k_1 + prices[i])
            dp_i_k_1 = max(dp_i_k_1, dp_i_kp1_0 - prices[i])
            dp_i_kp1_0 = max(dp_i_kp1_0, dp_i_kp1_1 + prices[i])
            dp_i_kp1_1 = max(dp_i_kp1_1, -prices[i])
        return dp_i_k_0


# k = any integer but k < len(prices), or equals to k = +infinity
class Solution6(object):
    def maxProfit(self, prices, k):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[[0.0, 0.0] for _ in range(k + 1)] for _ in range(len(prices))]
        for i in range(len(prices)):
            j = k
            while j >= 1:
                if i == 0:
                    dp[i][j][0] = 0
                    # 允许k次交易的情况下，第一天持有股票的收益
                    dp[i][j][1] = -prices[i]
                else:
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
                j -= 1
        print('dp: ', dp)
        return dp[-1][-1][0]


if __name__ == '__main__':
    # solution = Solution4()
    # print(solution.maxProfit(prices=[7,1,5,3,6,4], free=3))

    # solution = Solution5()
    # print(solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]))

    solution = Solution6()
    print(solution.maxProfit(prices=[1,2,3,0,2], k=1))
