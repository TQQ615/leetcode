"""
二维矩阵 grid由 0（土地）和 1（水）组成。岛是由最大的4个方向连通的 0组成的群，封闭岛是一个完全 由1包围（左、上、右、下）的岛。

请返回 封闭岛屿 的数目。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/number-of-closed-islands

eg1:
输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
输出：2
解释：
灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。

"""
from typing import Optional, List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        relt = 0

        def dfs(i, j):
            # 越界
            if i >= m or j >= n or i < 0 or j < 0:
                return
            if grid[i][j] == 1:
                # 已经是海水
                return
            # 淹掉：变成海水
            grid[i][j] = 1
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

        for i in range(m):
            # 淹掉
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            # 淹掉
            dfs(0, j)
            dfs(m - 1, j)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    relt += 1
                    dfs(i, j)
        return relt


if __name__ == '__main__':
    solution = Solution()
    grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    print(solution.closedIsland(grid))
