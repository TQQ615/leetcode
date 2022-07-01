from typing import List

"""
0-1背包问题：
给你一个可装载重量为 W 的背包和 N 个物品，
每个物品有重量和价值两个属性。
其中第 i 个物品的重量为 wt[i]，价值为 val[i]，现在让你用这个背包装物品，最多能装的价值是多少？
eg1:
N = 3, W = 4
wt = [2, 1, 3]
val = [4, 2, 3]
"""


def getRelt(N, W, wt, val):
    # dp[w][n]：可装重量为w，n个物品的背包，可装的最大价值是多少
    dp = [[0 for _ in range(N + 1)] for _ in range(W + 1)]
    # 对于 n = 0，最大价值是0，对于w = 0，最大价值也是0
    for i in range(1, W + 1):
        for j in range(1, N + 1):
            # 第j个物品的重量大于总重量
            if wt[j - 1] > i:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = max(
                    # 选择当前第j个物品
                    dp[i - wt[j - 1]][j - 1] + val[j - 1],
                    # 不选择当前第j个物品
                    dp[i][j - 1]
                )
    return dp[W][N]


N = 3
W = 4
wt = [2, 1, 2]
val = [4, 2, 3]
print(getRelt(N, W, wt, val))


"""MID
子集背包问题：
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

eg1:
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

eg2:
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。

转化：
给一个可装载重量为 sum / 2 的背包和 N 个物品，每个物品的重量为 nums[i]。现在让你装物品，是否存在一种装法，能够恰好将背包装满？
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 包的容量
        target = int(sum(nums) / 2)
        # 和为奇数时，直接返回False
        if target * 2 != sum(nums):
            return False
        # n个物品
        n = len(nums)
        # dp[i][j]表示：i个物品，j为最大容量，是否能刚好装满
        # dp[0][j]表示：0个物品，不能把背包装满，all False
        # dp[i][0]表示：背包容量为0，已经装满，all True
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j - nums[i - 1] < 0:
                    # 背包容量不足，装不下第i个物品，结果和不选i一样
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = (dp[i - 1][j - nums[i - 1]]) or (dp[i - 1][j])
                    # 选第i个物品：dp[i - 1][j - nums[i - 1]]
                    # 不选第i个物品：dp[i - 1][j]
        return dp[n][target]


# 空间复杂度优化：压缩成以为存储
class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        # 包的容量
        target = int(sum(nums) / 2)
        # 和为奇数时，直接返回False
        if target * 2 != sum(nums):
            return False
        # n个物品
        n = len(nums)
        # 记录对于每次遍历物品的时候，对于target是否能刚好装满
        dp = [False for _ in range(target + 1)]
        # 容量为0的时候，算已经装满，对于其他元素，认为初始没有物品，所以都不能装满
        dp[0] = True

        for i in range(n):
            # j 较大的状态依赖 上一个物品(i - 1)j较小的状态，所以从后往前更新
            for j in range(target, 0, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]]
        return dp[-1]


"""MID
完全背包问题
给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。

请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。

假设每一种面额的硬币有无限个。

题目数据保证结果符合 32 位带符号整数。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/coin-change-2

eg1:
输入：amount = 5, coins = [1, 2, 5]
输出：4
解释：有四种方式可以凑成总金额：
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

eg2:
输入：amount = 3, coins = [2]
输出：0
解释：只用面额 2 的硬币不能凑成总金额 3 。

eg3:
输入：amount = 10, coins = [10] 
输出：1

转化：
有一个背包，最大容量为 amount，有一系列物品 coins，每个物品的重量为 coins[i]，每个物品的数量无限。
请问有多少种方法，能够把背包恰好装满？

这个问题和我们前面讲过的两个背包问题，有一个最大的区别就是，每个物品的数量是无限的，这也就是传说中的「完全背包问题」，
没啥高大上的，无非就是状态转移方程有一点变化而已。
"""


class Solution3:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        if n <= 0:
            return 0
        # dp[i][j] 表示coins[0~i]中，可以凑成总金额j的方式，有多少种
        # dp[i][0] 总金额为0，什么都不选，是唯一的凑钱方法 !!!!!!!!!!!!!!!!!!!
        # dp[0][j] coins没有待选元素，总方式为0
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
                    # 选第i种硬币面值 dp[i][j - coins[i - 1]]
                    # 不选第i种硬币面值 dp[i - 1][j]
        return dp[-1][-1]


# 压缩空间复杂度
class Solution4:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        if n <= 0:
            return 0
        # dp[i] 表示对于coin中某个元素的遍历时存储的状态，即最多的凑钱方式
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for i in range(n):
            # 这里和前面一题不太一样，这里的状态转移是依赖本次元素(i) j较小的状态，所以从小到大开始更新
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    dp[j] = dp[j - coins[i]] + dp[j]
                    # 选第i种硬币面值 dp[j - coins[i - 1]]
                    # 不选第i种硬币面值 dp[j]
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.canPartition(nums = [1,5,10,6]))
    solution2 = Solution2()
    print(solution2.canPartition(nums = [1,5,10,6]))
    solution3 = Solution3()
    print(solution3.change(amount = 5, coins = [1, 2, 5]))
    print(solution3.change(amount = 10, coins = [10]))
    print(solution3.change(amount = 3, coins = [2]))
    solution4 = Solution4()
    print(solution4.change(amount = 5, coins = [1, 2, 5]))

