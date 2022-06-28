"""MID
给你两个字符串s1和s2 ，写一个函数来判断 s2 是否包含 s1的排列。如果是，返回 true ；否则，返回 false 。
换句话说，s1 的排列之一是 s2 的 子串 。

eg1:
输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").

eg2:
输入：s1= "ab" s2 = "eidboaoo"
输出：false

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/permutation-in-string
"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        target_dic = dict()
        interval = len(s1)
        exist_dic = dict()
        for k in s1:
            if k in target_dic.keys():
                target_dic[k] += 1
            else:
                target_dic[k] = 1
        l = 0
        r = interval - 1
        for i in range(interval):
            exist_dic[s2[i]] = exist_dic.get(s2[i], 0) + 1

        def check():
            for k in target_dic.keys():
                if exist_dic.get(k, 0) != target_dic[k]:
                    return False
            return True

        while r < len(s2):
            if check():
                return True
            exist_dic[s2[l]] -= 1
            l += 1
            r += 1
            if r < len(s2):
                exist_dic[s2[r]] = exist_dic.get(s2[r], 0) + 1
        return False


if __name__ == '__main__':
    solution = Solution()
    # print(solution.checkInclusion(s1="ab", s2="eidbaooo"))
    # print(solution.checkInclusion(s1="ab", s2="eidboaoo"))
    print(solution.checkInclusion(s1="ad", s2="a"))
