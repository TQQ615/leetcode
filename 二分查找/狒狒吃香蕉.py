"""
珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有piles[i]根香蕉。警卫已经离开了，将在 h 小时后回来。

珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。
如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/koko-eating-bananas

eg1:
输入：piles = [3,6,7,11], h = 8
输出：4

eg2:
输入：piles = [30,11,23,4,20], h = 5
输出：30

eg3:
输入：piles = [30,11,23,4,20], h = 6
输出：23
"""
from typing import Optional, List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = 10000000001

        # 以速度target吃piles的香蕉堆时，最快的时间
        def f(piles, target):
            hours = 0
            for i in range(len(piles)):
                hours += piles[i] // target
                if piles[i] % target != 0:
                    hours += 1
            return hours

        while left <= right:
            mid = left + (right - left) // 2
            if f(piles, mid) == h:
                right = mid - 1
            # 如果最快的时间还是超时了，则需要提高速度
            elif f(piles, mid) > h:
                left = mid + 1
            elif f(piles, mid) < h:
                right = mid - 1
        # 最快的时间可以小于限制时间
        return left if f(piles, left) <= h else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.minEatingSpeed(piles = [3,6,7,11], h = 8))
    print(solution.minEatingSpeed(piles = [30, 11, 23, 4, 20], h = 5))
    print(solution.minEatingSpeed(piles = [30,11,23,4,20], h = 6))
    print(solution.minEatingSpeed([312884470], 312884469))
    print(solution.minEatingSpeed([1000000000],2))
