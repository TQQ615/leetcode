"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

eg1:
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10

eg2:
输入： heights = [2,4]
输出： 4
"""
from typing import Optional, List


class Solution:
    """
    单调栈
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # left[i]表示：第i个元素左边小于height[i]的最近的idex
        left = [0 for _ in range(n)]
        # right[i]表示：第i个元素右边小于height[i]的最近的idex
        right = [0 for _ in range(n)]
        # 单调栈：从栈顶到栈低元素是单调递增的，用来找到第i个元素最近的元素id
        stack = []
        for i in range(n):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = -1 if len(stack) == 0 else stack[-1]
            stack.append(i)

        stack = []
        for j in range(n - 1, -1, -1):
            while len(stack) > 0 and heights[stack[-1]] >= heights[j]:
                stack.pop()
            right[j] = n if len(stack) == 0 else stack[-1]
            stack.append(j)
        # left[i] ~ right[i]之间都是heights高于heights[i]的，可以计算idx之差作为宽来计算面积
        return max([(right[i] - left[i] - 1) * heights[i] for i in range(n)])


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestRectangleArea([2,1,5,6,2,3]))
