"""
给你一个整数数组nums和一个整数k，请你返回 非空子序列元素和的最大值，
子序列需要满足：子序列中每两个 相邻的整数nums[i]和nums[j]，
它们在原数组中的下标i和j满足i < j且 j - i <= k 。

数组的子序列定义为：将数组中的若干个数字删除（可以删除 0 个数字），剩下的数字按照原本的顺序排布。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/constrained-subsequence-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

eg1:
输入：nums = [10,2,-10,5,20], k = 2
输出：37
解释：子序列为 [10, 2, 5, 20] 。

eg2:
输入：nums = [-1,-2,-3], k = 1
输出：-1
解释：子序列必须是非空的，所以我们选择最大的数字。

eg3:
输入：nums = [10,-2,-10,-5,20], k = 2
输出：23
解释：子序列为 [10, -2, -5, 20] 。
"""
from typing import Optional, List


class Solution:
    # 动态规划: 超时
    def constrainedSubsetSum1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 定义状态矩阵：dp[i]表示：nums[0...i]中，选中nums[i]的时候满足限制的子序列中和最大值
        dp = [0 for _ in range(n)]

        for i in range(n):
            # dp[i] = nums[i]
            start = max(0, i - k)
            for j in range(start, i):
                dp[i] = max(dp[i], dp[j])
            dp[i] += nums[i]
        return max(dp)

    # 动态规划 + 单调栈
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 定义状态矩阵：dp[i]表示：nums[0...i]中，选中nums[i]的时候满足限制的子序列中和最大值
        dp = [0 for _ in range(n)]
        # 单调栈，存储距当前k步之内dp[.]的从大到小的序列
        stack = [0]
        dp[0] = nums[0]

        for i in range(1, n):
            while len(stack) > 0 and stack[0] < i - k:
                stack.pop(0)
            # 可以不选前面k个dp[.]中的元素，这里表现为max(0, dp[.])
            dp[i] = max(0, dp[stack[0]]) + nums[i]

            while len(stack) > 0 and dp[stack[-1]] <= dp[i]:
                stack.pop()
            stack.append(i)
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.constrainedSubsetSum(nums = [10,2,-10,5,20], k = 2))
    print(solution.constrainedSubsetSum(nums = [-1,-2,-3], k = 1))
    print(solution.constrainedSubsetSum(nums = [10,-2,-10,-5,20], k = 2))