"""
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/shortest-unsorted-continuous-subarray

eg1:
输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

eg2:
输入：nums = [1,2,3,4]
输出：0
"""
from typing import Optional, List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = -1
        right = -1
        max_val = - float("inf")
        min_val = float("inf")
        for i in range(n):
            if max_val > nums[i]:
                right = i
            else:
                max_val = nums[i]

            if min_val < nums[n - 1 - i]:
                left = n - 1 - i
            else:
                min_val = nums[n - 1 - i]
        # print('right: ', right)
        return 0 if right == -1 else right - left + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.findUnsortedSubarray([2,6,4,8,10,9,15]))
    print(solution.findUnsortedSubarray([1,2,3,4]))


