"""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/word-break

eg1:
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

eg2:
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
    注意，你可以重复使用字典中的单词。

eg3:
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""
from typing import Optional, List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 错误的解法，对于有些情况没法完成
        # i = 0
        # while i < len(s):
        #     ori_i = i
        #     for word in wordDict:
        #         length = len(word)
        #         if i + length > len(s):
        #             continue
        #         elif s[i: i + length] == word:
        #             if i + length == len(s):
        #                 return True
        #             else:
        #                 i += length
        #         else:
        #             continue
        #     if ori_i == i:
        #         return False

        # 正确的解法：动态规划：需要尝试所有的待选字符匹配：
        memo = [-1 for _ in range(len(s))]
        
        def dp(i):
            if i == len(s):
                return True
            if i > len(s):
                return False
            if memo[i] != -1:
                return True if memo[i] == 1 else False
            for word in wordDict:
                j = i + len(word)
                if s[i:j] == word and dp(j):
                    memo[i] = 1
                    return True
                else:
                    continue
            memo[i] = 0
            return False

        return dp(0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))
    print(solution.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
    print(solution.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
    print(solution.wordBreak("cars", ["ca","car","rs"]))
    print(solution.wordBreak("cars", ["car","ca","rs"]))
