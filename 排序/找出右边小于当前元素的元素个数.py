"""
给你一个整数数组 nums ，按要求返回一个新数组counts 。
数组 counts 有该性质： counts[i] 的值是 nums[i] 右侧小于nums[i] 的元素的数量。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/count-of-smaller-numbers-after-self

eg1:
输入：nums = [5,2,6,1]
输出：[2,1,1,0]
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素

eg2:
输入：nums = [-1]
输出：[0]
"""
# TODO: 按照labuladong的java版本直接翻译过来的，没通过所有测试用例，待查
from typing import Optional, List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0 for _ in range(n)]
        ori_nums = [nums[i] for i in range(len(nums))]
        # counts = dict()

        def merge(num_list, left, mid, right):
            temp = [_ for _ in num_list]
            i = left
            j = mid + 1
            for p in range(left, right + 1):
                if i == mid + 1:
                    num_list[p] = temp[j]
                    j += 1
                elif j == right + 1:
                    num_list[p] = temp[i]
                    i += 1
                    counts[ori_nums.index(num_list[p])] += j - mid - 1
                elif temp[i] > temp[j]:
                    num_list[p] = temp[j]
                    j += 1
                else:
                    num_list[p] = temp[i]
                    i += 1
                    counts[ori_nums.index(num_list[p])] += j - mid - 1

        def sort(nums, start, end):
            if start == end:
                return
            mid = start + (end - start) // 2
            sort(nums, start, mid)
            sort(nums, mid + 1, end)
            merge(nums, start, mid, end)

        sort(nums, 0, n - 1)
        return counts


if __name__ == '__main__':
    solution = Solution()
    print(solution.countSmaller([5, 2, 6, 1]))
    print(solution.countSmaller([-1, -1]))
