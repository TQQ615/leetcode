"""MID
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-palindromic-subsequence

eg1:
输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。

eg2:
输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。
"""


#  dp 数组的定义是：在子串 s[i..j] 中，最长回文子序列的长度为 dp[i][j]。
# 找状态转移需要归纳思维，说白了就是如何从已知的结果推出未知的部分，这样定义容易归纳，容易发现状态转移关系。
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for k in range(n):
            # 在子串 s[k] 中，最长回文子序列的长度为 1。
            dp[k][k] = 1

        for j in range(1, n):
            # 注意更新方式
            # for i in range(j - 1, -1, -1):
            #     if s[i] == s[j]:
            #         # 如果s[i] == s[j]， 它俩一定在最长回文子序列中
            #         dp[i][j] = dp[i + 1][j - 1] + 2
            #     else:
            #         # 否则选择加入任意一个字符中最大的那个
            #         dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            for l in range(n - j):
                if s[l] == s[j + l]:
                    # 如果s[i] == s[j]， 它俩一定在最长回文子序列中
                    dp[l][j + l] = dp[l + 1][j + l - 1] + 2
                else:
                    # 否则选择加入任意一个字符中最大的那个
                    dp[l][j + l] = max(dp[l + 1][j + l], dp[l][j + l - 1])
        return dp[0][n - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindromeSubseq(s = "bbbab"))

