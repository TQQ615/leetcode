"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。

eg1:
输入：nums = [1,1,1], k = 2
输出：2

eg2:
输入：nums = [1,2,3], k = 3
输出：2
"""
from typing import Optional, List


class Solution:
    # 枚举: 复杂度O(n^2)，超出时间复杂度
    def subarraySum1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        relt = 0
        for i in range(n):
            sum_ = 0
            for j in range(i, n):
                sum_ += nums[j]
                if sum_ == k:
                    relt += 1
                    continue
        return relt

    # 前缀和&哈希表
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 哈希表记录求和为key的不同子数组的个数(value)
        sum_map = dict()
        sum_map.update({0: 1})
        n = len(nums)
        # 列表记录nums[:i + 1]的前缀和
        sum_list = [0 for _ in range(n + 1)]
        relt = 0
        for i in range(1, n + 1):
            sum_list[i] = sum_list[i - 1] + nums[i - 1]
            relt += sum_map.get(sum_list[i] - k, 0)
            sum_map[sum_list[i]] = sum_map.get(sum_list[i], 0) + 1
        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.subarraySum([1,1,1], 2))
    print(solution.subarraySum([1,2,3], 3))