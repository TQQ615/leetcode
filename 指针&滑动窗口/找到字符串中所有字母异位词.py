"""
给定两个字符串s和 p，找到s中所有p的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-all-anagrams-in-a-string

eg1:
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

eg2:
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。

"""
from typing import Optional, List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns = len(s)
        np = len(p)

        left = 0
        right = 0

        need_dic = dict()
        for pp in p:
            need_dic[pp] = need_dic.get(pp, 0) + 1
        window = dict()
        relt = []

        while right < ns:
            window[s[right]] = window.get(s[right], 0) + 1

            while right - left >= np:
                window[s[left]] = window.get(s[left], 0) - 1
                left += 1
            flag = 1
            for k, v in need_dic.items():
                if window.get(k, 0) != v:
                    flag = 0
                    break
            if flag == 1:
                relt.append(left)
            right += 1
        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.findAnagrams(s = "abab", p = "ab"))
    print(solution.findAnagrams(s = "cbaebabacd", p = "abc"))




