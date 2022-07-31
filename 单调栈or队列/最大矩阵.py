"""
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

eg1:
输入：matrix =
[
["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]
]
输出：6
解释：最大矩形如上图所示。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/maximal-rectangle

eg2:
输入：matrix = [["0"]]
输出：0

eg3:
输入：matrix = [["0","0"]]
输出：0
"""
from typing import Optional, List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        # 计算matrix[i][j]元素左边有多少个连续的1
        left = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    left[i][j] = left[i][j - 1] + 1 if j > 0 else 1

        relt = 0
        for i in range(m):
            for j in range(n):
                # 逐个元素往上面的行check最大面积
                height = left[i][j]
                area = left[i][j]
                for k in range(i - 1, -1, -1):
                    # 多行之间取最小的长度
                    height = min(height, left[k][j])
                    area = max(area, height * (i - k + 1))
                relt = max(relt, area)
        return relt


if __name__ == '__main__':
    solution = Solution()
    matrix = \
    [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(solution.maximalRectangle(matrix))

