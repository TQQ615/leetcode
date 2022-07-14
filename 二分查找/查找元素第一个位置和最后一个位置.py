"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回[-1, -1]。

你必须设计并实现时间复杂度为O(log n)的算法解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array

eg1:
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
"""
from typing import Optional, List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftMost(nums, target):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            return left if left < len(nums) and target == nums[left] else -1

        def rightMost(nums, target):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            return left - 1 if left > 0 and nums[left - 1] == target else -1

        return [leftMost(nums, target), rightMost(nums, target)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange(nums = [5,7,7,8,8,10], target = 8))


