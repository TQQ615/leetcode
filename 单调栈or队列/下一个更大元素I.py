"""
nums1中数字x的 下一个更大元素 是指x在nums2 中对应位置 右侧 的 第一个 比x大的元素。

给你两个 没有重复元素 的数组nums1 和nums2 ，下标从 0 开始计数，其中nums1是nums2的子集。

对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。
如果不存在下一个更大元素，那么本次查询的答案是 -1 。

返回一个长度为nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/next-greater-element-i

eg1:
输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
输出：[-1,3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
- 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
- 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。

eg2:
输入：nums1 = [2,4], nums2 = [1,2,3,4].
输出：[3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 2 ，用加粗斜体标识，nums2 = [1,2,3,4]。下一个更大元素是 3 。
- 4 ，用加粗斜体标识，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1 。
"""
from typing import Optional, List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def getNextGreater(nums):
            n = len(nums)
            stack = []
            relt = [0 for _ in range(n)]

            for i in range(n - 1, -1, -1):
                while len(stack) > 0 and stack[-1] < nums[i]:
                    stack.pop()
                relt[i] = stack[-1] if len(stack) > 0 else -1
                stack.append(nums[i])
            return relt

        relt = getNextGreater(nums2)
        return [relt[nums2.index(nums1[i])] for i in range(len(nums1))]


if __name__ == '__main__':
    solution = Solution()
    print(solution.nextGreaterElement([2,4], [1,2,3,4]))

