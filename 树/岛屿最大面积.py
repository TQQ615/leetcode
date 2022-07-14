"""
给你一个大小为 m x n 的二进制矩阵 grid 。

岛屿是由一些相邻的1(代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。
你可以假设grid 的四个边缘都被 0（代表水）包围着。

岛屿的面积是岛上值为 1 的单元格的数目。

计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/max-area-of-island

eg1:
输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
输出：6
解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。

"""
from typing import Optional, List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        relt = 0

        def dfs(i, j):
            # 越界
            if i >= m or j >= n or i < 0 or j < 0:
                return 0
            if grid[i][j] == 0:
                # 已经是海水
                return 0
            # 淹掉：变成海水
            grid[i][j] = 0
            return dfs(i - 1, j) + \
            dfs(i, j - 1) + \
            dfs(i + 1, j) + \
            dfs(i, j + 1) + 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    relt = max(relt, dfs(i, j))

        return relt


if __name__ == '__main__':
    solution = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(solution.maxAreaOfIsland(grid))
