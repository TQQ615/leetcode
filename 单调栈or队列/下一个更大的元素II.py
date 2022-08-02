"""
给定一个循环数组nums（nums[nums.length - 1]的下一个元素是nums[0]），返回nums中每个元素的 下一个更大元素 。

数字 x的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
如果不存在，则输出 -1。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/next-greater-element-ii

eg1:
输入: nums = [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

eg2:
输入: nums = [1,2,3,4,3]
输出: [2,3,4,-1,4]
"""
from typing import Optional, List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        relt = [0 for _ in range(n)]

        for i in range(2 * n - 1, -1, -1):
            # 有相等元素的情况，需要把和自己一样大的元素pop掉
            while len(stack) > 0 and stack[-1] <= nums[i % n]:
                stack.pop()
            relt[i % n] = stack[-1] if len(stack) > 0 else -1
            stack.append(nums[i % n])
        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.nextGreaterElements([1,2,3,4,3]))

