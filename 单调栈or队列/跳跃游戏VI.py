"""
给你一个下标从 0 开始的整数数组 nums和一个整数 k。

一开始你在下标0处。每一步，你最多可以往前跳k步，但你不能跳出数组的边界。
也就是说，你可以从下标i跳到[i + 1， min(n - 1, i + k)]包含 两个端点的任意位置。

你的目标是到达数组最后一个位置（下标为 n - 1），你的 得分为经过的所有数字之和。

请你返回你能得到的 最大得分。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/jump-game-vi

eg1:
输入：nums = [1,-1,-2,4,-7,3], k = 2
输出：7
解释：你可以选择子序列 [1,-1,4,3] （上面加粗的数字），和为 7 。

eg2:
输入：nums = [10,-5,-2,4,0,3], k = 3
输出：17
解释：你可以选择子序列 [10,4,3] （上面加粗数字），和为 17 。

eg3:
输入：nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
输出：0
"""
from typing import Optional, List


class Solution:
    # 动态规划
    def maxResult1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-100 for _ in range(n)]
        dp[0] = nums[0]

        for i in range(1, n):
            start = max(0, i - k)
            for j in range(start, i):
                dp[i] = max(dp[i], dp[j] + nums[i])
        return dp[-1]

    # 单调栈
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-100 for _ in range(n)]
        dp[0] = nums[0]
        stack = [0]

        for i in range(1, n):
            while stack[0] < i - k:
                stack.pop(0)
            dp[i] = dp[stack[0]] + nums[i]

            while len(stack) > 0 and dp[stack[-1]] <= dp[i]:
                stack.pop()
            stack.append(i)
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxResult(nums = [1,-5,-20,4,-1,3,-6,-3], k = 2))
    print(solution.maxResult(nums = [10,-5,-2,4,0,3], k = 3))
    print(solution.maxResult(nums = [1,-1,-2,4,-7,3], k = 2))
    print(solution.maxResult([100,-100,-300,-300,-300,-100,100], 4))
