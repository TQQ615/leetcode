"""
集合 s 包含从 1 到n的整数。不幸的是，因为数据错误，
导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/set-mismatch

eg1:
输入：nums = [1,2,2,4]
输出：[2,3]

eg2:
输入：nums = [1,1]
输出：[1,2]
"""
from typing import Optional, List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        relt = []
        # 用idx对应的值的正负来标记：这个idx + 1对应的值是否存在，存在则记录为负；
        # 这里对于已经记录过的idx对应的值，需要取abs(.)来防止idx溢出
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                relt.append(idx + 1)
            else:
                nums[idx] *= (-1)
        for i in range(len(nums)):
            if nums[i] > 0:
                relt.append(i + 1)
        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.findErrorNums([1,2,2,4]))
    print(solution.findErrorNums(nums = [3,2,2]))