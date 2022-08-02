"""
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/perfect-squares

eg1:
输入：n = 12
输出：3
解释：12 = 4 + 4 + 4

eg2:
输入：n = 13
输出：2
解释：13 = 4 + 9
"""
import math


class Solution:
    # 超时
    def numSquares1(self, n: int) -> int:

        def f(n):
            s = math.sqrt(n)
            s_low = math.floor(s)
            if s == s_low:
                return 1
            relt = float("inf")
            for i in range(1, s_low + 1):
                relt = min(relt, f(n - i ** 2) + 1)
            return relt
        return f(n)

    def numSquares2(self, n: int) -> int:
        f = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            j = 1
            relt = float("inf")
            while j ** 2 <= i:
                relt = min(relt, f[i - j ** 2] + 1)
                j += 1
            f[i] = relt
        return f[-1]

    # 四平方和定理：https://baike.baidu.com/item/%E5%9B%9B%E5%B9%B3%E6%96%B9%E5%92%8C%E5%AE%9A%E7%90%86
    def numSquares(self, n: int) -> int:
        def isPerfectSquare(n):
            s = math.sqrt(n)
            s_low = math.floor(s)
            if s == s_low:
                return True
            return False

        def checkAnswer4(n):
            while n % 4 == 0:
                n = n / 4
            return n % 8 == 7

        if isPerfectSquare(n):
            return 1
        if checkAnswer4(n):
            return 4
        i = 1
        while i ** 2 < n:
            b = n - i ** 2
            if isPerfectSquare(b):
                return 2
            i += 1
        return 3


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSquares(12))
    print(solution.numSquares(13))
