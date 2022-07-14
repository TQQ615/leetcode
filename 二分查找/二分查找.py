"""
给定一个n个元素有序的（升序）整型数组nums 和一个目标值target ，写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-search

eg1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

eg2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1

"""
from typing import Optional, List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            # print('mid:', mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1

    # 左闭右开
    # def leftMostSearch(self, nums: List[int], target: int) -> int:
    #     left = 0
    #     right = len(nums) # TODO
    #
    #     while left < right:
    #         mid = left + (right - left) // 2
    #         if nums[mid] == target:
    #             right = mid # TODO
    #         elif nums[mid] < target:
    #             left = mid + 1
    #         elif nums[mid] > target:
    #             right = mid
    #     return left if left < len(nums) and nums[left] == target else -1 # TODO

    # 两端闭合
    def leftMostSearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1 # TODO
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        return left if left < len(nums) and nums[left] == target else -1 # TODO

    # 左开右闭
    # def rightMostSearch(self, nums: List[int], target: int) -> int:
    #     left = 0
    #     right = len(nums)
    #
    #     while left < right:
    #         mid = left + (right - left) // 2
    #         if nums[mid] == target:
    #             left = mid + 1 # TODO
    #         elif nums[mid] < target:
    #             left = mid + 1
    #         elif nums[mid] > target:
    #             right = mid
    #     return left - 1 if nums[left - 1] == target else -1 # TODO

    # 两端闭合
    def rightMostSearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1 # TODO
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return left - 1 if left > 0 and nums[left - 1] == target else -1 # TODO


if __name__ == '__main__':
    solution = Solution()
    print(solution.search(nums = [-1,0,3,5,9,12], target = 9))
    print(solution.search(nums = [-1,0,3,5,9,12], target = 2))
    print(solution.leftMostSearch(nums=[1,2,2,2,3], target=2))
    print(solution.rightMostSearch(nums=[1,2,2,2,3], target=2))
