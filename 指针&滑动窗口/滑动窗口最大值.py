"""
给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/sliding-window-maximum

eg1:
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

eg2:
输入：nums = [1], k = 1
输出：[1]
"""
from typing import Optional, List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        relt = []

        # 单调队列：保证队列里是单调递减的关系，当出现较大的元素的时候，删掉前面小于他的元素，保证单调性
        def pushStack(x):
            while len(stack) > 0 and stack[-1] < x:
                stack.pop()
            stack.append(x)

        # 从滑动窗口出去的元素，同时需要从队列里删除，防止结果错误
        def popStack(x):
            if x == stack[0]:
                stack.pop(0)

        for i in range(n):
            if i < k - 1:
                pushStack(nums[i])
            else:
                pushStack(nums[i])
                relt.append(stack[0])
                popStack(nums[i - k + 1])

        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
    print(solution.maxSlidingWindow(nums = [1], k = 1))
