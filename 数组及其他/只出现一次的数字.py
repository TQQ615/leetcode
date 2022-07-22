"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/single-number
eg1:
输入: [2,2,1]
输出: 1
"""
from typing import Optional, List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([2,2,1]))