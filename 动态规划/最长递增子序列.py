"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-increasing-subsequence

eg1:
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

eg2:
输入：nums = [0,1,0,3,2,3]
输出：4
"""


# 时间复杂度： O(N^2)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        max_len = 1
        for k in dp:
            if k > max_len:
                max_len = k
        return max_len

# TODO 贪心+二分查找


# 扩展到二维
"""HARD
给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。

当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

注意：不允许旋转信封。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/russian-doll-envelopes

eg1:  
输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

eg2:
输入：envelopes = [[1,1],[1,1],[1,1]]
输出：1
"""


# 超时，待优化
class Solution2(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        sorted_envelopes = sorted(envelopes, key=lambda x:(x[0], -x[1]))
        dp = [1] * len(sorted_envelopes)
        for i in range(len(sorted_envelopes)):
            for j in range(i):
                if sorted_envelopes[j][1] < sorted_envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        max_len = 1
        for k in dp:
            if max_len < k:
                max_len = k
        return max_len


if __name__ == '__main__':
    # solution = Solution()
    # print(solution.lengthOfLIS([10,9,2,5,3,7,101,18]))
    solution = Solution2()
    print(solution.maxEnvelopes([[1,1],[1,1],[1,1]]))
