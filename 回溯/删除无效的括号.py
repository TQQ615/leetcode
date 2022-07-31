"""
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

返回所有可能的结果。答案可以按 任意顺序 返回。

eg1:
输入：s = "()())()"
输出：["(())()","()()()"]

eg2:
输入：s = "(a)())()"
输出：["(a())()","(a)()()"]

eg3:
输入：s = ")("
输出：[""]
"""
from typing import Optional, List


class Solution:
    # 回溯
    def removeInvalidParentheses1(self, s: str) -> List[str]:
        lremove = 0
        rremove = 0
        relt = []
        # 计算有多少个落单的括号需要删除的
        for ss in s:
            if ss == '(':
                lremove += 1
            if ss == ')':
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1

        # 判断字符串是否合法的括号
        def isValid(s):
            cnt = 0
            for ss in s:
                if ss == '(':
                    cnt += 1
                if ss == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def helper(s, start, lremove, rremove):
            if lremove == 0 and rremove == 0:
                # 如果合法，加入结果列表
                if isValid(s):
                    relt.append(s)
                return
            for i in range(start, len(s)):
                # 剪枝：对于连续相同的括号符号，不需要重复计算：因为删掉前一个或者后一个最终结果是一样的
                if i > start and s[i] == s[i - 1]:
                    continue
                # 需要删除的字符个数大于剩下的字符个数，无需计算了，不满足
                if lremove + rremove > len(s) - i:
                    break
                # 落单的有'('，并且当前元素相同时，尝试删除
                if lremove > 0 and s[i] == '(':
                    helper(s[:i] + s[i + 1:], i, lremove - 1, rremove)
                # 落单的有')'，并且当前元素相同时，尝试删除
                if rremove > 0 and s[i] == ')':
                    helper(s[:i] + s[i + 1:], i, lremove, rremove - 1)
                # TODO 不尝试当前元素不删除吗？
                #  有尝试，在for循环里面：遍历下一个元素时,lremove和rremove没有减少，即前面的元素不删除！！！

        helper(s, 0, lremove, rremove)
        return relt

    # 广度优先遍历, 时间复杂度更高，尝试每一个删除，没有事先计算最少删除数量
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            cnt = 0
            for ss in s:
                if ss == '(':
                    cnt += 1
                elif ss == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        current_set = {s}
        relt = []

        while True:
            for ss in current_set:
                if isValid(ss):
                    relt.append(ss)
            if len(relt) > 0:
                return relt
            next_set = set()
            for ss in current_set:
                for i in range(len(ss)):
                    # 保证不删除多的括号对
                    if i > 0 and ss[i] == ss[i - 1]:
                        continue
                    if ss[i] in ('(', ')'):
                        next_set.add(ss[:i] + ss[i + 1:])
            current_set = next_set


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeInvalidParentheses("()())()"))
    print(solution.removeInvalidParentheses("(a)())()"))
    print(solution.removeInvalidParentheses("()())()"))
    print(solution.removeInvalidParentheses("(()"))
    print(solution.removeInvalidParentheses(")("))
