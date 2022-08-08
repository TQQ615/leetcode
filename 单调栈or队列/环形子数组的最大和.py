"""
给定一个长度为 n 的环形整数数组nums，返回nums的非空 子数组 的最大可能和。

环形数组意味着数组的末端将会与开头相连呈环状。
形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i]的前一个元素是 nums[(i - 1 + n) % n] 。

子数组 最多只能包含固定缓冲区nums中的每个元素一次。形式上，对于子数组nums[i], nums[i + 1], ..., nums[j]，
不存在i <= k1, k2 <= j其中k1 % n == k2 % n。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/maximum-sum-circular-subarray

eg1:
输入：nums = [1,-2,3,-2]
输出：3
解释：从子数组 [3] 得到最大和 3

eg2:
输入：nums = [5,-3,5]
输出：10
解释：从子数组 [5,5] 得到最大和 5 + 5 = 10

eg3:
输入：nums = [3,-2,2,-3]
输出：3
解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
"""
from typing import Optional, List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        # 前缀和
        P = [nums[0]]
        for i in range(1, 2 * n):
            P.append(P[i - 1] + nums[i % n])

        # 考虑最大的 P_j - P_i，其中 j - i <= N。 考虑第 j 个候选答案：对于固定 j 的最优结果 P_j - P_i
        # 我们希望一个 i 使得 P_i尽量小 并且满足 j−N ≤ i < j，称对于第 j 个候选答案的的最优 i。可以用优先队列实现它。
        stack = [0]
        ans = nums[0]
        for i in range(1, 2 * n):
            # print('i: ', i, ' n: ', n)
            if stack[0] < i - n:
                stack.pop(0)

            ans = max(ans, P[i] - P[stack[0]])

            while len(stack) > 0 and P[i] <= P[stack[-1]]:
                stack.pop()
            stack.append(i)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubarraySumCircular([5,-3,5]))



