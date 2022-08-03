"""
给定一个包含n + 1 个整数的数组nums ，其数字都在[1, n]范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-the-duplicate-number

eg1:
输入：nums = [1,3,4,2,2]
输出：2

eg2:
输入：nums = [3,1,3,4,2]
输出：3
"""
from typing import Optional, List


class Solution:
    # 我们定义 cnt[i] 表示 nums 数组中小于等于 i 的数有多少个，
    # 假设我们重复的数是 target，那么 [1,target−1]里的所有数满足 cnt[i]≤i，[target,n] 里的所有数满足 cnt[i]>i，具有单调性。
    # 二分法
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 1
        right = n - 1
        relt = 0
        while left <= right:
            mid = left + (right - left) // 2
            cnt = 0
            for i in range(n):
                if nums[i] <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid - 1
                relt = mid
        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.findDuplicate([1,3,4,2,2]))
