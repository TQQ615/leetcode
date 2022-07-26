"""
给你一个整数数组 nums 。玩家 1 和玩家 2 基于这个数组设计了一个游戏。

玩家 1 和玩家 2 轮流进行自己的回合，玩家 1 先手。开始时，两个玩家的初始分值都是 0 。
每一回合，玩家从数组的任意一端取一个数字（即，nums[0] 或 nums[nums.length - 1]），取到的数字将会从数组中移除（数组长度减 1 ）。
玩家选中的数字将会加到他的得分上。当数组中没有剩余数字可取时，游戏结束。

如果玩家 1 能成为赢家，返回 true 。如果两个玩家得分相等，同样认为玩家 1 是游戏的赢家，也返回 true 。你可以假设每个玩家的玩法都会使他的分数最大化。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/predict-the-winner

eg1:
输入：nums = [1,5,2]
输出：false
解释：一开始，玩家 1 可以从 1 和 2 中进行选择。
如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。
所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
因此，玩家 1 永远不会成为赢家，返回 false 。

eg2:
输入：nums = [1,5,233,7]
输出：true
解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 true，表示玩家 1 可以成为赢家。

"""
from typing import Optional, List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # 建立状态矩阵，每个元素dp[i][j]是一个元组，分别是(先手，后手)对于nums[i:j + 1]的最大游戏收益
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        # 边界条件: 只有nums[i]时先手得分，后手分数为0
        for i in range(n):
            dp[i][i] = [nums[i], 0]

        # 状态转移矩阵：
        for l in range(1, n):
            for i in range(n - l):
                j = i + l
                # 先手选左边的收益 > 先手选右边的收益
                if dp[i + 1][j][1] + nums[i] > dp[i][j - 1][1] + nums[j]:
                    dp[i][j][0] = dp[i + 1][j][1] + nums[i]
                    # 如果选了左边这一堆，后手就成了右边这一堆的先手
                    dp[i][j][1] = dp[i + 1][j][0]
                else:
                    dp[i][j][0] = dp[i][j - 1][1] + nums[j]
                    dp[i][j][1] = dp[i][j - 1][0]
        return dp[0][n - 1][0] >= dp[0][n - 1][1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.PredictTheWinner([1,5,233,7]))
    print(solution.PredictTheWinner([1,5,2]))

