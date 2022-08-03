"""
给定一个m x n 二维字符网格board 和一个字符串单词word 。如果word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格
同一个单元格内的字母不允许被重复使用。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/word-search

eg1:
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

eg2:
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true

eg3:
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false

"""
from typing import Optional, List


class Solution:
    def __init__(self):
        self.find = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)
        visited = [[0 for _ in range(n)] for _ in range(m)]

        def backtrace(i, j, k):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if visited[i][j] == 1 or self.find or board[i][j] != word[k]:
                return False
            if k == l - 1:
                # self.find = True
                return True

            visited[i][j] = 1
            return backtrace(i - 1, j, k + 1) or \
            backtrace(i + 1, j, k + 1) or \
            backtrace(i, j - 1, k + 1) or \
            backtrace(i, j + 1, k + 1)

        relt = False
        for ii in range(m):
            for jj in range(n):
                relt = relt or backtrace(ii, jj, 0)

        return relt #self.find


if __name__ == '__main__':
    solution = Solution()
    print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
    print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))
    print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))