"""
给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和'*'的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/regular-expression-matching

eg1:
输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。

eg2:
输入：s = "aa", p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

eg3:
输入：s = "ab", p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

"""


class Solution:
    # 常规匹配，迭代难以实现，需要升级
    # def isMatch1(self, s: str, p: str) -> bool:
    #     i = 0
    #     j = 0
    #     ns = len(s)
    #     np = len(p)
    #
    #     while i < ns and j < np:
    #         if s[i] == p[j] or p[j] == '.':
    #             if j + 1 < np and p[j + 1] == '*':
    #                 # 考虑 * 可以匹配0次或者多次
    #                 # 尝试 匹配0次
    #                 if j + 2 < np and p[j + 2] == s[i]:
    #                     j += 2
    #                 # 尝试 匹配多次
    #                 print(i, j)
    #             else:
    #                 # 无法匹配多个字符串，只匹配单个，往后移动i, j
    #                 i += 1
    #                 j += 1
    #         else:
    #             if j + 1 < np and p[j + 1] == '*':
    #                 # 有 * 只考虑匹配0次
    #                 j += 2
    #             else:
    #                 # 没有 *通配符，无法匹配下去
    #                 return False

    # 动态规划
    def isMatch2(self, s: str, p: str) -> bool:
        ns = len(s)
        np = len(p)
        # print('ns: ', ns, 'np: ', np)

        # 含义是：s[i:] 和 p[j:] 是否匹配
        def dp(s, i, p, j):
            # 停止条件
            if j == np:
                return i == ns
            if i == ns:
                if (np - j) % 2 == 1:
                    return False
                for k in range(j + 1, np, 2):
                    if p[k] != '*':
                        return False
                return True

            # 当前的单个字符可以匹配
            if s[i] == p[j] or p[j] == '.':
                # 如果p后面有 * 通配符：
                if j + 1 < np and p[j + 1] == '*':
                    # 匹配0次 or 匹配多次
                    return dp(s, i, p, j + 2) or dp(s, i + 1, p, j)
                # p后面没有 * 通配符，只能往后check
                else:
                    return dp(s, i + 1, p, j + 1)
            # 当前的单个字符不能匹配
            else:
                # 后面是否有 * 通配符 可以拯救？
                if j + 1 < np and p[j + 1] == '*':
                    # 匹配s[i] 0次
                    return dp(s, i, p, j + 2)
                # 没有 * 通配符，没救了，不匹配
                else:
                    return False

        return dp(s, 0, p, 0)

    # 动态规划: 添加备忘录
    def isMatch(self, s: str, p: str) -> bool:
        ns = len(s)
        np = len(p)
        mome = dict()

        def dp(s, i, p, j):
            # 停止条件
            if j == np:
                return i == ns
            if i == ns:
                if (np - j) % 2 == 1:
                    return False
                for k in range(j + 1, np, 2):
                    if p[k] != '*':
                        return False
                return True
            if (i, j) in mome.keys():
                return mome[(i, j)]

            res = False
            # 当前字符是否可以匹配：
            if s[i] == p[j] or p[j] == '.':
                # 后面有#
                if j + 1 < np and p[j + 1] == '*':
                    # 匹配0次 or 匹配多次
                    res = dp(s, i, p, j + 2) or dp(s, i + 1, p, j)
                else:
                    res = dp(s, i + 1, p, j + 1)
            else:
                if j + 1 < np and p[j + 1] == '*':
                    res = dp(s, i, p, j + 2)
                else:
                    res = False
            mome[(i, j)] = res
            return res

        return dp(s, 0, p, 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch(s = "aa", p = "a*"))
    print(solution.isMatch(s = "ab", p = ".*"))
    print(solution.isMatch(s = "aa", p = "a"))
    print(solution.isMatch("aab", "c*a*b"))
