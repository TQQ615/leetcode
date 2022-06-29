"""
给你一个 n x n 的 方形 整数数组matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。

下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。
在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。
具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-falling-path-sum

eg1:
输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
输出：13
解释：如图所示，为和最小的两条下降路径

eg2:
输入：matrix = [[-19,57],[-40,-5]]
输出：-59
解释：如图所示，为和最小的下降路径
"""


class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[0] = matrix[0]
        for i in range(1, n):
            for j in range(n):
                min_list = list()
                for k in range(-1, 2):
                    if 0 <= j + k < n:
                        min_list.append(dp[i - 1][j + k])
                dp[i][j] = matrix[i][j] + min(min_list)
        return min(dp[-1][:])


if __name__ == '__main__':
    solution = Solution()
    print(solution.minFallingPathSum([[-19,57],[-40,-5]]))
