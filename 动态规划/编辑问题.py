"""HARD
给你两个单词word1 和word2， 请返回将word1转换成word2 所使用的最少操作数。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/edit-distance

eg1:
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

eg2:
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[1 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        # print('dp', dp)
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        # print('dp', dp)
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min([
                        # 删除操作：解释：对于当前word2字段j, 结果和word1的i - 1字符一致(i被放弃)，表示word1该字符i被删掉
                        dp[i - 1][j] + 1,
                        # 插入操作：解释：对于当前word1字段i, 结果和word2的j - 1字符一致(j被放弃)，表示word2该字符j被插入
                        dp[i][j - 1] + 1,
                        # 替换操作：解释：
                        dp[i - 1][j - 1] + 1
                    ])
        # print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance(word1 = "intention", word2 = "execution"))