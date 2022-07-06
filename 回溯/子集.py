"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

eg1:
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

eg2:
输入：nums = [0]
输出：[[],[0]]

"""
from typing import Optional, List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        relt = list()

        def backtrace(relt_e, idx):
            if idx == len(nums):
                relt.append([_ for _ in relt_e])
                return
            # 不选该元素
            backtrace(relt_e, idx + 1)
            # 选该元素
            relt_e.append(nums[idx])
            backtrace(relt_e, idx + 1)
            relt_e.pop()
        backtrace([], 0)
        return relt


"""
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/subsets-ii

eg1:
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

eg2:
输入：nums = [0]
输出：[[],[0]]
"""


class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        relt = list()
        nums = sorted(nums)

        def backtrace(relt_e, idx):
            if idx == len(nums):
                # TODO trick，未剪枝，或者不需剪枝
                if relt_e not in relt:
                    relt.append([_ for _ in relt_e])
                return

            backtrace(relt_e, idx + 1)

            relt_e.append(nums[idx])
            backtrace(relt_e, idx + 1)
            relt_e.pop()

        backtrace([], 0)
        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets(nums = [1,2,3]))

    solution = Solution2()
    print(solution.subsetsWithDup(nums = [1,2,2]))