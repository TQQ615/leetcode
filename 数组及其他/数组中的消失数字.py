"""
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。
请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array

eg1:
输入：nums = [4,3,2,7,8,2,3,1]
输出：[5,6]

eg2:
输入：nums = [1,1]
输出：[2]

"""
from typing import Optional, List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        repeated = []
        lacked = []
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                repeated.append(idx + 1)
            else:
                nums[idx] *= (-1)
        for i in range(n):
            if nums[i] > 0:
                lacked.append(i + 1)
        return repeated, lacked


if __name__ == '__main__':
    solution = Solution()
    print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1])[:])
    print(solution.findDisappearedNumbers([1,1])[:])
    print(solution.findDisappearedNumbers([4,3,2,7,7,2,3,1])[:])
