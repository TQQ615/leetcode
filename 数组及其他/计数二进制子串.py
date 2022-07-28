"""
给定一个字符串s，统计并返回具有相同数量 0 和 1 的非空（连续）子字符串的数量，
并且这些子字符串中的所有 0 和所有 1 都是成组连续的。

重复出现（不同位置）的子串也要统计它们出现的次数。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/count-binary-substrings

eg1:
输入：s = "00110011"
输出：6
解释：6 个子串满足具有相同数量的连续 1 和 0 ："0011"、"01"、"1100"、"10"、"0011" 和 "01" 。
注意，一些重复出现的子串（不同位置）要统计它们出现的次数。
另外，"00110011" 不是有效的子串，因为所有的 0（还有 1 ）没有组合在一起。

eg2:
输入：s = "10101"
输出：4
解释：有 4 个子串："10"、"01"、"10"、"01" ，具有相同数量的连续 1 和 0 。
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        counts = [1]
        relt = 0
        for i in range(1, n):
            if s[i] == s[i - 1]:
                counts[-1] += 1
            else:
                counts.append(1)
        for j in range(len(counts) - 1):
            relt += min(counts[j], counts[j + 1])
        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.countBinarySubstrings("00110011"))
    print(solution.countBinarySubstrings("10101"))
