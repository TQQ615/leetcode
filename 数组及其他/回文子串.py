"""
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。

回文字符串 是正着读和倒过来读一样的字符串。

子字符串 是字符串中的由连续字符组成的一个序列。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/palindromic-substrings

eg1:
输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"

eg2:
输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        # 状态矩阵：dp[i][j]表示第1个字符到第j个字符是否是回文子串
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        # 对角线上第l层
        for l in range(1, n):
            # 从第i=0开始更新矩阵，第l层只更新 n - l 个数
            for i in range(n - l):
                j = i + l
                if s[i] == s[j]:
                    if i + 1 <= j - 1 and dp[i + 1][j - 1] == 1:
                        dp[i][j] = 1
                    elif i == j - 1:
                        dp[i][j] = 1

        return sum([sum(dp[i]) for i in range(n)])


if __name__ == '__main__':
    solution = Solution()
    print(solution.countSubstrings("abc"))
    print(solution.countSubstrings("aaaaa"))
