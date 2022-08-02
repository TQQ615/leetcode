"""
给你一个整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加'+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/target-sum

eg1:
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

eg2:
输入：nums = [1], target = 1
输出：1
"""
from typing import Optional, List


class Solution:
    def __init__(self):
        self.relt = 0

    # 基本回溯
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if len(nums) == 0:
            return 0

        def dp(nums, idx, target):
            if idx == n - 1:
                if nums[idx] == abs(target):
                    self.relt += 1
                return

            dp(nums, idx + 1, target - nums[idx])
            dp(nums, idx + 1, target + nums[idx])

        dp(nums, 0, target)
        return self.relt

    # 添加备忘录
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if len(nums) == 0:
            return 0
        memo = dict()

        def dp(idx, target):
            # 这里有边界条件没有满足的情况，比如最后一位是0，+0 、-0是两种方案，这里会漏掉
            # if idx == n - 1:
            #     if nums[idx] == abs(target):
            #         return 1
            #     return 0
            if idx == n:
                if target == 0:
                    return 1
                return 0
            if (idx, target) in memo.keys():
                return memo.get((idx, target))

            res = dp(idx + 1, target + nums[idx]) + dp(idx + 1, target - nums[idx])
            memo[(idx, target)] = res
            return res

        return dp(0, target)

    # 动态规划：
    # 如果我们把 nums 划分成两个子集 A 和 B，分别代表分配 + 的数和分配 - 的数，那么他们和 target 存在如下关系：
    # sum(A) - sum(B) = target
    # sum(A) = target + sum(B)
    # sum(A) + sum(A) = target + sum(B) + sum(A)
    # 2 * sum(A) = target + sum(nums)
    # ==>
    # sum(A) = (target + sum(nums)) / 2
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if len(nums) == 0:
            return 0

        sum_ = sum(nums)
        sum_a = (target + sum_) // 2
        if sum_a * 2 != target + sum_:
            return 0
        if sum_a < 0:
            return 0
        # dp[i][j]表示：截止到第i个元素，和为j的组合有多少种
        dp = [[0 for _ in range(1 + sum_a)] for _ in range(1 + n)]
        # 边界条件
        # 显然 dp[0][..] = 0，因为没有物品的话，根本没办法装背包；
        # 但是 dp[0][0] 应该是个例外，因为如果背包的最大载重为 0，「什么都不装」也算是一种装法，即 dp[0][0] = 1。
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(sum_a + 1):
                # print('i = ', i, " j = ", j)
                if nums[i - 1] > j:
                    # 第i个元素加入超过j，只能不选
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j]
        # print('dp: ', dp)
        return dp[n][sum_a]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))
    print(solution.findTargetSumWays([1,0], 1))
    print(solution.findTargetSumWays([0,0,0,0,0,0,0,0,1], 1))
    print(solution.findTargetSumWays([100], -200))
