"""
给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。

eg1:
输入：n = 2
输出：[0,1,1]
解释：
0 --> 0
1 --> 1
2 --> 10

eg2:
输入：n = 5
输出：[0,1,1,2,1,2]
解释：
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

"""
from typing import Optional, List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0]
        high_bit = 0
        for i in range(1, n + 1):
            # 如果是1bit数，更新high_bit
            if i & (i - 1) == 0:
                high_bit = i
            # i 比 i - high_bit 多一个1bit位
            bits.append(bits[i - high_bit] + 1)
        return bits


if __name__ == '__main__':
    solution = Solution()
    print(solution.countBits(5))
