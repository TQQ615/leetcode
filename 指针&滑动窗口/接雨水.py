"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/trapping-rain-water

eg1:
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

"""
from typing import Optional, List

"""
water[i] = min(
           # 左边最高的柱子
           max(height[0..i]),
           # 右边最高的柱子
           max(height[i..end])
        ) - height[i]
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        relt = 0
        n = len(height)
        lmax = [0 for _ in range(n)]
        rmax = [0 for _ in range(n)]
        lmax[0] = height[0]
        rmax[n-1] = height[n - 1]
        for i in range(1, n):
            lmax[i] = max(lmax[i - 1], height[i])
        for j in range(n - 2, -1, -1):
            rmax[j] = max(rmax[j + 1], height[j])
        for i in range(1, n - 1):
            relt += min(lmax[i], rmax[i]) - height[i]
        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
