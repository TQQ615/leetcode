"""
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

eg1:
输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。

eg2:
输入: nums = [1,2,3,4], k = 3
输出: false

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/partition-to-k-equal-sum-subsets
"""
from typing import Optional, List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k > len(nums):
            return False
        sum_all = sum(nums)
        if sum_all % k != 0:
            return False
        target = sum_all / k
        # 标记第i个元素是否被使用
        used = [0 for _ in range(len(nums))]
        # 记录已经遍历过的组合，直接使用其结果
        used_state = dict()

        def backtrace(k, nums, target, used, bucket, start_idx):
            if k == 0:
                return True
            if bucket == target:
                relt = backtrace(k - 1, nums, target, used, 0, 0)
                used_state["".join(str(used))] = relt
                return relt
            if "".join(str(used)) in used_state.keys():
                return used_state["".join(str(used))]
            for i in range(start_idx, len(nums)):
                if used[i] == 1:
                    continue
                if bucket + nums[i] > target:
                    continue
                bucket += nums[i]
                used[i] = 1
                if backtrace(k, nums, target, used, bucket, i + 1):
                    return True
                used[i] = 0
                bucket -= nums[i]
            return False

        return backtrace(k, nums, target, used, 0, 0)


if __name__ == '__main__':
    solution = Solution()
    # print(solution.canPartitionKSubsets(nums = [4, 3, 2, 3, 5, 2, 1], k = 4))
    # print(solution.canPartitionKSubsets(nums = [1,2,3,4], k = 3))
    # print(solution.canPartitionKSubsets([1,1,1,1,2,2,2,2],4))
    print(solution.canPartitionKSubsets([2,9,4,7,3,2,10,5,3,6,6,2,7,5,2,4],7))

