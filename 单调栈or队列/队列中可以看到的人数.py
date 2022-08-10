"""
有n个人排成一个队列，从左到右编号为0到n - 1。给你以一个整数数组heights，每个整数 互不相同，heights[i]表示第i个人的高度。

一个人能 看到 他右边另一个人的条件是这两人之间的所有人都比他们两人 矮。
更正式的，第i个人能看到第j个人的条件是i < j且min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1])。

请你返回一个长度为 n的数组answer，其中answer[i]是第i个人在他右侧队列中能看到的人数。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/number-of-visible-people-in-a-queue

eg1:
输入：heights = [10,6,8,5,11,9]
输出：[3,1,2,1,1,0]
解释：
第 0 个人能看到编号为 1 ，2 和 4 的人。
第 1 个人能看到编号为 2 的人。
第 2 个人能看到编号为 3 和 4 的人。
第 3 个人能看到编号为 4 的人。
第 4 个人能看到编号为 5 的人。
第 5 个人谁也看不到因为他右边没人。

eg2:
输入：heights = [5,1,2,3,10]
输出：[4,1,1,1,0]
"""
from typing import Optional, List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)

        stack = []
        relt = [0 for _ in range(n)]

        for i in range(n - 1, -1, -1):
            while len(stack) > 0:
                relt[i] += 1
                if heights[i] > heights[stack[-1]]:
                    stack.pop()
                else:
                    break
            stack.append(i)

        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.canSeePersonsCount(heights = [10,6,8,5,11,9]))
