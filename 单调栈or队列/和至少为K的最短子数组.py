"""
给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。
如果不存在这样的 子数组 ，返回 -1 。

子数组 是数组中 连续 的一部分。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k

eg1:
输入：nums = [1], k = 1
输出：1

eg2:
输入：nums = [1,2], k = 4
输出：-1

eg3:
输入：nums = [2,-1,2], k = 3
输出：3
"""
from typing import Optional, List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 前缀和数组，辅助寻找答案：当P[j] - P[i] >= k (i < j)时，最小的 j - i + 1
        # 对于某一个固定的j来说，找 最近满足 P[j] - P[i] >= k (i < j) 的 i=opt(j)
        # 求所有的 j - opt(j) + 1 的最小值
        P = [0]
        for i in range(n):
            P.append(P[-1] + nums[i])
        print('P: ', P)
        # 单调队列：维护当前元素j来说满足 P[j] - P[i] >= k (i < j) 的i,
        # 按照P[i]递增来存储，越往后P[i]越大，越不能满足条件：P[j] - P[i] >= k，
        # 删除掉比P[i]大且比i更远的idex，不能满足且更远
        stack = [0]
        relt = n + 1

        for j in range(n + 1):
            # 满足约束，则进一步check更大更近的
            while len(stack) > 0 and P[stack[0]] <= P[j] - k:
                relt = min(relt, j - stack[0])
                # 用完pop掉是因为 j + 1如果也和i满足，那么没有 j - i 优秀
                stack.pop(0)

            # 保持栈内的单调性，更远更大的不会比当前更满足
            while len(stack) > 0 and P[stack[-1]] >= P[j]:
                stack.pop()
            stack.append(j)

        return relt if relt < n + 1 else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestSubarray(nums = [2,-1,2], k = 3))
    print(solution.shortestSubarray(nums = [1,2], k = 4))
    print(solution.shortestSubarray(nums = [1], k = 1))