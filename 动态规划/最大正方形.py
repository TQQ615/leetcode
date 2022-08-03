"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

eg1:
输入：matrix = [
["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]
]
输出：4

eg2:
输入：matrix = [["0","1"],["1","0"]]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/maximal-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import Optional, List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        relt = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            relt = max(relt, dp[i][0] ** 2)
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            relt = max(relt, dp[0][j] ** 2)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    relt = max(relt, dp[i][j] ** 2)
        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximalSquare(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(solution.maximalSquare(matrix = [["0","1"],["1","0"]]))
