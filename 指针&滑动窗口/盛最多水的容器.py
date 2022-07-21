"""
给定一个长度为 n 的整数数组height。有n条垂线，第 i 条线的两个端点是(i, 0)和(i, height[i])。

找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/container-with-most-water
"""
from typing import Optional, List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        relt = 0
        i = 0
        j = len(height) - 1
        hh = 0
        while i < j:
            if height[i] < height[j]:
                min_idx = i
            else:
                min_idx = j
            if height[min_idx] > hh:
                h = height[min_idx]
                relt = max(relt, h * (j - i))
                hh = h
            if min_idx == i:
                    i += 1
            else:
                    j -= 1
        return relt