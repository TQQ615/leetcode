"""
matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
输出：1,2,3,4,8,12,11,10,9,5,6,7

给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

eg1:
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

eg2:
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
"""
from typing import Optional, List


# 通过
def f(matrix):
    m = len(matrix)
    n = len(matrix[0])
    relt = []
    for i in range((m + 1) // 2):
        print('i=', i)
        for j in range(i, n - i):
            relt.append(matrix[i][j])
        if i > n - 1 - i:
            break
        for k in range(i + 1, m - i - 1):
            relt.append(matrix[k][n - 1 - i])
        if i == (m + 1) // 2 - 1 and m % 2 != 0:
            break
        for j in range(n - 1 - i, i - 1, -1):
            relt.append(matrix[m - 1 - i][j])
        if i >= n - 1 - i:
            break
        for k in range(m - 2 - i, i, -1):
            relt.append(matrix[k][i])
    return relt


# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(f(matrix))
#
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# print(f(matrix))
#
# matrix = [[7], [9], [6]]
# print(f(matrix))

matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
print(f(matrix))


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        column = len(matrix[0])
        left = 0
        right = column - 1
        top = 0
        bottom = row - 1
        relt = []
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                relt.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                relt.append(matrix[i][right])
            if left < right and top < bottom:
                for i in range(right - 1, left, -1):
                    relt.append(matrix[bottom][i])
                for i in range(bottom, top, -1):
                    relt.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return relt


if __name__ == '__main__':
    solution = Solution()
    matrix = \
    [
        # [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]
        [1, 2, 3], [4, 5, 6], [7, 8, 9]
    ]
    # print(solution.spiralOrder(matrix))
