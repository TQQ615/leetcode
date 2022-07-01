from typing import List

"""MID
括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

eg1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

eg2:
输入：n = 1
输出：["()"]

"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        relt = list()
        left = 0
        right = 0

        def backtrace(s, ll, rr):
            if ll == n and rr == n:
                relt.append("".join(s))
                return
            if ll < rr:
                return
            if ll > n or rr > n:
                return
            s.append("(")
            backtrace(s, ll + 1, rr)
            s.pop()

            s.append(")")
            backtrace(s, ll, rr + 1)
            s.pop()

        s = list()
        backtrace(s, left, right)
        return relt


"""EASY
有效括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/valid-parentheses

eg1:
输入：s = "()[]{}"
输出：true

eg2:
输入：s = "([)]"
输出：false
"""


class Solution2:
    def isValid(self, s: str) -> bool:
        stack = list()
        for ss in s:
            if ss in ("(", "[", "{"):
                stack.append(ss)
            elif len(stack) > 0:
                check = stack.pop()
                if (check == "(" and ss != ")") or (check == "[" and ss != "]") or (check == "{" and ss != "}"):
                    return False
            else:
                return False
        if len(stack) > 0:
            return False
        return True





if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))
    solution = Solution2()
    print(solution.isValid(s = "()[]{}"))
