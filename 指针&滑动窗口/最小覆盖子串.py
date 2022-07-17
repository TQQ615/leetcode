"""HARD
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：
对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。

eg1:
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"

eg2:
输入：s = "a", t = "a"
输出："a"

eg3:
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-window-substring

框架：
int left = 0, right = 0;
while (right < s.size()) {` // 增大窗口
    window.add(s[right]);
    right++;
    while (window needs shrink) { // 缩小窗口
            window.remove(s[left]);
    left++; }
}

"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target_dic = dict()
        exist_dic = dict()
        for k in t:
            if k in target_dic.keys():
                target_dic[k] += 1
            else:
                target_dic[k] = 1
        l = 0
        r = -1
        ansL = -1
        ansR = -1
        length = float("inf")

        def check():
            for k in target_dic.keys():
                if exist_dic.get(k, 0) < target_dic[k]:
                    return False
            return True

        while r < len(s) - 1:
            r += 1
            exist_dic[s[r]] = exist_dic.get(s[r], 0) + 1
            while check() and l <= r:
                if r - l + 1 < length:
                    length = r - l + 1
                    ansL = l
                exist_dic[s[l]] -= 1
                l += 1
        return s[ansL:ansL + length] if ansL != -1 else ""


if __name__ == '__main__':
    solution = Solution()
    # s = "ADOBECODEBANC"
    # print(s[1])
    # print(solution.minWindow(s="ADOBECODEBANC", t="ABC"))
    # print(solution.minWindow(s="a", t="aa"))
    print(solution.minWindow(s="a", t="a"))


