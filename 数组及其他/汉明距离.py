"""
两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。

给你两个整数 x 和 y，计算并返回它们之间的汉明距离。
eg1:
输入：x = 1, y = 4
输出：2
解释：
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置

eg2:
输入：x = 3, y = 1
输出：1
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 取异或，当且仅当该位上不一致是返回1
        s = x ^ y
        relt = 0
        while s != 0:
            s = s & (s - 1)
            relt += 1
        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingDistance(x = 3, y = 1))
