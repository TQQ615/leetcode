"""
整数数组的一个 排列 就是将其所有成员以序列或线性顺序排列。

例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。
更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，
那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。
如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
给你一个整数数组 nums ，找出 nums 的下一个排列。

必须 原地 修改，只允许使用额外常数空间！！！

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/next-permutation

eg1:
输入：nums = [1,2,3]
输出：[1,3,2]

eg2:
输入：nums = [3,2,1]
输出：[1,2,3]

eg3:
输入：nums = [1,1,5]
输出：[1,5,1]

eg4:
输入：[4,5,2,6,3,1]
输出：[4,5,3,1,2,6]
"""
from typing import Optional, List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        # 首先从后向前查找第一个顺序对 (i,i+1)(i,i+1)，满足 a[i] < a[i+1]a[i]<a[i+1]。
        # 这样「较小数」即为 a[i]a[i]。此时 [i+1,n)[i+1,n) 必然是下降序列。
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # 这里需要区分nums[0] < nums[1](后序从1开始逆转) 还是 nums[0] > nums[1](从0开始逆转)
        if i >= 0:
            # 如果找到了顺序对，那么在区间 [i+1,n)[i+1,n) 中从后向前查找第一个元素 j 满足 a[i] < a[j]。
            # 这样「较大数」即为 a[j]。\
            j = n - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            print('j: ', j)
            # 交换 a[i]a[i] 与 a[j]a[j]，此时可以证明区间 [i+1,n)[i+1,n) 必为降序。
            # 我们可以直接使用双指针反转区间 [i+1,n)[i+1,n) 使其变为升序，而无需对该区间进行排序。
            nums[i], nums[j] = nums[j], nums[i]
        # 直接使用双指针反转区间 [i+1,n)[i+1,n) 使其变为升序，而无需对该区间进行排序。
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    solution = Solution()
    # nums = [4,5,2,6,3,1]
    # solution.nextPermutation(nums)
    # print(nums)

    n2 = [5,1,1]
    solution.nextPermutation(n2)
    print(n2)

    # n3 = [1, 3, 2]
    # solution.nextPermutation(n3)
    # print(n3)
    # #
    # n4 = [3, 2, 1]
    # solution.nextPermutation(n4)
    # print(n4)
    #
    # n5 = [5, 4, 3, 2, 1]
    # solution.nextPermutation(n5)
    # print(n5)

