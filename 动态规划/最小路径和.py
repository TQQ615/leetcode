"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

eg1:
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

eg2:
输入：grid = [[1,2,3],[4,5,6]]
输出：12
"""
from typing import Optional, List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        dp = [[10000 for _ in range(columns)] for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for i in range(rows):
            for j in range(columns):
                if i == 0 and j == 0:
                    continue
                left = max(i - 1, 0)
                up = max(j - 1, 0)
                dp[i][j] = min(dp[left][j], dp[i][up]) + grid[i][j]
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))
    print(solution.minPathSum(grid = [[1,2,3],[4,5,6]]))
