"""
给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。

请你找出并返回只出现一次的那个数。

你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/single-element-in-a-sorted-array

eg1:
输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2

eg2:
输入: nums =  [3,3,7,7,10,11,11]
输出: 10
"""
from typing import Optional, List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        while left <= right:
            mid = left + (right - left) // 2
            if mid == len(nums) - 1 and nums[mid] != nums[mid - 1]:
                return nums[mid]
            if mid == 0 and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    right = mid - 2
                if nums[mid] == nums[mid + 1]:
                    left = mid + 2
            if mid % 2 == 1:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                if nums[mid] == nums[mid + 1]:
                    right = mid - 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
    print(solution.singleNonDuplicate([3,3,7,7,10,11,11]))
    print(solution.singleNonDuplicate([1,1,2]))
