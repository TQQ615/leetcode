"""
给你一个整数数组nums，返回 数组answer，其中answer[i]等于nums中除nums[i]之外其余各元素的乘积。

题目数据 保证 数组nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内。

请不要使用除法，且在O(n) 时间复杂度内完成此题。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/product-of-array-except-self

eg1:
输入: nums = [1,2,3,4]
输出: [24,12,8,6]

eg2:
输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
"""
from typing import Optional, List


class Solution:
    # 初始化 answer 数组，对于给定索引 i，answer[i] 代表的是 i 左侧所有数字的乘积。
    # 构造方式与之前相同，只是我们试图节省空间，先把 answer 作为方法一的 L 数组。
    # 这种方法的唯一变化就是我们没有构造 R 数组。而是用一个遍历来跟踪右边元素的乘积。
    # 并更新数组 answer[i]=answer[i]*Ranswer[i]=answer[i]∗R。
    # 然后 R 更新为 R=R*nums[i]R=R∗nums[i]，其中变量 R 表示的就是索引右侧数字的乘积。
    #
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1 for _ in range(n)]
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        R = 1
        for j in range(n - 1, -1, -1):
            answer[j] = answer[j] * R
            R = R * nums[j]
        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.productExceptSelf([1,2,3,4]))
    print(solution.productExceptSelf([-1,1,0,-3,3]))
