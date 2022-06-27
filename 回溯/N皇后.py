""" HARD
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n皇后问题 研究的是如何将 n个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的n皇后问题 的解决方案。

每一种解法包含一个不同的n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/n-queens

eg:
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

框架：
def backtrack(...):
    for 选择 in 选择列表:
        做选择
        backtrack(...)
        撤销选择
"""


# 循序渐进：
# /* 主函数，输入一组不重复的数字，返回它们的全排列 */
from typing import List


def arrangement(nums):
    relt = list()

    def backtrace(nums, ll):
        if len(nums) == len(ll):
            # 这里不能直接append，否则后面ll.pop()对这里的结果也生效；
            # 参考https://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html
            relt.append([x for x in ll])
            return
        for i in nums:
            if i in ll:
                continue
            ll.append(i)
            backtrace(nums, ll)
            ll.pop()

    ll = list()
    backtrace(nums, ll)
    return relt


# 全部遍历
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        relt = list()
        relt_element = list()
        used_nums = list()

        def backtrace(used_nums, relt_element):
            if len(used_nums) == n:
                if is_valid(used_nums):
                    relt.append(["".join(_) for _ in relt_element])
                return
            for i in range(n):
                if i in used_nums:
                    continue
                used_nums.append(i)
                relt_line = ["."] * n
                relt_line[i] = 'Q'
                relt_element.append(relt_line)
                backtrace(used_nums, relt_element)
                relt_element.pop()
                used_nums.pop()

        def is_valid(used_nums):
            exist_list = list()
            for i, j in zip(range(n), used_nums):
                exist_list.append([i, j])
            for x in exist_list:
                no_valid_idx = list()
                for p in range(-1, 2):
                    for q in range(-1, 2):
                        # 四周
                        no_valid_idx.append([x[0] + p, x[1] + q])
                for k in range(2, n):
                    # 对角线
                    no_valid_idx.append([x[0] + k, x[1] + k])
                    no_valid_idx.append([x[0] - k, x[1] - k])
                    no_valid_idx.append([x[0] - k, x[1] + k])
                    no_valid_idx.append([x[0] + k, x[1] - k])
                no_valid_idx.remove(x)
                for c in exist_list:
                    if c in no_valid_idx:
                        return False
            return True

        backtrace(used_nums, relt_element)
        return relt


# 仅填充遍历
class Solution2(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        relt = list()
        used_nums = list()

        def backtrace(used_nums):
            if len(used_nums) == n and is_valid(used_nums):
                relt_element = list()
                for k in used_nums:
                    relt_line = ["."] * n
                    relt_line[k] = 'Q'
                    relt_element.append("".join(relt_line))
                relt.append(relt_element)
                return
            for i in range(n):
                if (not is_valid(used_nums)) or (i in used_nums):
                    continue
                used_nums.append(i)
                backtrace(used_nums)
                used_nums.pop()

        def is_valid(used_nums):
            if len(used_nums) <= 1:
                return True
            i0 = len(used_nums) - 1
            j0 = used_nums[-1]
            exist_list = list()
            for i, j in zip(range(len(used_nums) - 1), used_nums[:-1]):
                exist_list.append([i, j])
            no_valid_idx = list()
            for k in range(1, n):
                # 左上
                no_valid_idx.append([i0 - k, j0 - k])
                # 右上
                no_valid_idx.append([i0 - k, j0 + k])
            for c in exist_list:
                if c in no_valid_idx:
                    return False
            return True

        backtrace(used_nums)
        return relt


class Solution3:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    # row - 列下标 = 固定值（左斜线）
                    # row + 列下表标 = 固定值（右斜线
                    # 参考：https://leetcode.cn/problems/n-queens/solution/nhuang-hou-by-leetcode-solution/
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n
        backtrack(0)
        return solutions


if __name__ == '__main__':
    # rr = arrangement([1,2,3])
    # print(rr)
    solution = Solution3()
    print(solution.solveNQueens(4))

