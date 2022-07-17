"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

eg1:
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

eg2:
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

"""
from typing import Optional, List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farest = 0
        for i in range(len(nums)):
            farest = max(farest, i + nums[i])
            if farest <= i:
                return False
        return farest >= len(nums) - 1


"""
给你一个非负整数数组nums ，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/jump-game-ii

eg1:
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
    从下标为 0 跳到下标为 1 的位置，跳1步，然后跳3步到达数组的最后一个位置。

eg2:
输入: nums = [2,3,0,1,4]
输出: 2
"""


class Solution2:
    # 动态规划
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums) + 1 for _ in range(len(nums))]
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    dp[i + j] = min(dp[i] + 1, dp[i + j])
            # print('dp:', dp)
        return dp[-1]

    # 贪心算法
    def jump2(self, nums: List[int]) -> int:
        farest = 0
        end = 0
        jump = 0
        for i in range(len(nums) - 1):
            farest = max(farest, i + nums[i])
            if end == i:
                end = farest
                jump += 1
            # print('i:', i, 'nums[i]:', nums[i], 'farest:', farest, 'jump:', jump)
        return jump


if __name__ == '__main__':
    solution = Solution()
    print(solution.canJump(nums = [2,3,1,1,4]))
    print(solution.canJump(nums = [3,2,1,0,4]))

    solution2 = Solution2()
    print(solution2.jump(nums = [2,3,1,1,4]))
    print(solution2.jump(nums = [2,3,0,1,4]))

    print(solution2.jump2(nums = [2,3,1,1,4]))
    print(solution2.jump2(nums = [2,3,0,1,4]))
