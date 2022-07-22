"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为O(n) 的算法解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-consecutive-sequence

eg1:
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

eg2:
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""
from typing import Optional, List


# 思路：对于每个元素，逐个+1，检验是否在数组里，但是复杂度O(n^2)
# 简化：对于原list元素去重，and 检查过的进行剪枝
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in num_set:

            if num - 1 not in num_set:
                current_num = num
                current_long = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_long += 1
                longest = max(longest, current_long)
        return longest


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestConsecutive([100,4,200,1,3,2]))
    print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
