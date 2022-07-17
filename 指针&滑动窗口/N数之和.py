"""
两数之和

给你一个下标从 1 开始的整数数组numbers ，该数组已按 非递减顺序排列 ，请你从数组中找出满足相加之和等于目标数target 的两个数。
如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。

以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。

你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

你所设计的解决方案必须只使用常量级的额外空间。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted

eg1:
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。

eg2:
输入：numbers = [2,3,4], target = 6
输出：[1,3]
解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。

eg3:
输入：numbers = [-1,0], target = -1
输出：[1,2]
解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。

"""
from typing import Optional, List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1
        relt = []

        while lo < hi:
            ss = numbers[lo] + numbers[hi]
            if ss == target:
                relt += [lo + 1, hi + 1]
                break
            elif ss > target:
                hi -= 1
            elif ss < target:
                lo += 1
        return relt

    # nums中可能有多对儿元素之和都等于target，请你的算法返回所有和为
    # target的元素对儿，其中不能出现重复。
    # eg1:
    # 输入为nums = [1, 3, 1, 2, 2, 3], target = 4，那么算法返回的结果就是：[[1, 3], [2, 2]]。
    def twoSum2(self, numbers: List[int], target: int) -> List[List[int]]:
        numbers = sorted(numbers)
        lo = 0
        hi = len(numbers) - 1
        relt = []

        while lo < hi:
            ss = numbers[lo] + numbers[hi]
            left = numbers[lo]
            right = numbers[hi]
            if ss == target:
                if [numbers[lo], numbers[hi]] not in relt:
                    relt.append([numbers[lo], numbers[hi]])
                while lo < hi and numbers[lo] == left:
                    lo += 1
                while lo < hi and numbers[hi] == right:
                    hi -= 1
            if ss > target:
                while lo < hi and numbers[hi] == right:
                    hi -= 1
            if ss < target:
                while lo < hi and numbers[lo] == left:
                    lo += 1
        return relt


"""
三数之和：
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？
请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/3sum

eg1:
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

eg2:
输入：nums = []
输出：[]
"""


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        final_relt = []

        def twoSum(nums, target):
            lo = 0
            hi = len(nums) - 1
            relt = []

            while lo < hi:
                ss = nums[lo] + nums[hi]
                left = nums[lo]
                right = nums[hi]
                if ss == target:
                    relt.append([nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == left:
                        lo += 1
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                elif ss < target:
                    while lo < hi and nums[lo] == left:
                        lo += 1
                elif ss > target:
                    while lo < hi and nums[hi] == right:
                        hi -= 1
            return relt
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            ll = twoSum(nums[i + 1:], 0 - nums[i])
            # print("i:", i, "nums[i]: ", nums[i], " two_sum:", ll)
            if len(ll) > 0:
                for k in ll:
                    final_relt.append([nums[i]] + k)
        return final_relt


"""
给你一个由 n 个整数组成的数组nums ，和一个目标值 target 。
请你找出并返回满足下述全部条件且不重复的四元组[nums[a], nums[b], nums[c], nums[d]]
（若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d< n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/4sum

eg1:
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

eg2:
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
"""


class Solution3:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        def nSum(nums, target, n):
            relt = []

            if n == 2:
                lo = 0
                hi = len(nums) - 1

                while lo < hi:
                    ss = nums[lo] + nums[hi]
                    left = nums[lo]
                    right = nums[hi]

                    if ss == target:
                        relt.append([nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == left:
                            lo += 1
                        while lo < hi and nums[hi] == right:
                            hi -= 1
                    elif ss > target:
                        while lo < hi and nums[hi] == right:
                            hi -= 1
                    elif ss < target:
                        while lo < hi and nums[lo] == left:
                            lo += 1
                return relt
            else:
                for i in range(len(nums) - 1):
                    ll = nSum(nums[i + 1:], target - nums[i], n - 1)
                    if i > 0 and nums[i] == nums[i - 1]:
                        continue
                    for k in ll:
                        relt.append([nums[i]] + k)
            return relt
        return nSum(nums, target, 4)


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum(numbers = [2,7,11,15], target = 9))
    print(solution.twoSum2(numbers = [1, 3, 1, 2, 2, 3], target = 4))

    solution2 = Solution2()
    print(solution2.threeSum(nums = [-1,0,1,2,-1,-4]))
    print(solution2.threeSum([1,2,-2,-1]))

    solution3 = Solution3()
    print(solution3.fourSum(nums = [1,0,-1,0,-2,2], target = 0))
    print(solution3.fourSum(nums = [2,2,2,2,2], target = 8))
