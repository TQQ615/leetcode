"""
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像3a或2[4]的输入。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/decode-string

eg1:
输入：s = "3[a]2[bc]"
输出："aaabcbc"

eg2:
输入：s = "3[a2[c]]"
输出："accaccacc"

eg3:
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"

eg4:
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
"""


class Solution:
    # 堆栈实现
    def decodeString1(self, s: str) -> str:
        stack = []
        n = len(s)
        relt = ''
        num_list = [str(i) for i in range(10)]
        str_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        i = 0
        while i < n:
            ss = s[i]
            if ss in str_list or ss == '[':
                stack.append(ss)
            elif ss in num_list:
                stack.append(ss)
            # 遇到了 ]
            else:
                substr = ''
                numstr = ''

                while stack[-1] != '[':
                    substr = stack[-1] + substr
                    stack.pop()
                stack.pop()
                while len(stack) > 0 and stack[-1] in num_list:
                    numstr = stack[-1] + numstr
                    stack.pop()
                sub_relt = ''
                for k in range(int(numstr)):
                    sub_relt += substr
                stack.append(sub_relt)
            i += 1
        # print('stack: ', stack)
        while len(stack) > 0:
            relt = stack.pop() + relt

        return relt

    # 递归实现
    def decodeString(self, s: str) -> str:
        num_list = [str(i) for i in range(10)]
        str_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]

        def backtrace(ss):
            n = len(ss)
            first_left_idx = -1
            last_right_idx = n
            num_str = ''
            pre_str = ''
            stack = []
            for i in range(n):
                if ss[i] in str_list:
                    if len(stack) == 0:
                       pre_str += ss[i]
                if ss[i] in num_list:
                    if len(stack) == 0:
                        num_str = ss[i] + num_str
                if ss[i] == '[':
                    stack.append(i)
                if ss[i] == ']':
                    if len(stack) > 1:
                        stack.pop()
                    else:
                        first_left_idx = stack[-1]
                        last_right_idx = i
                        break

            if first_left_idx == -1 and last_right_idx == n:
                return ss
            in_str = backtrace(ss[first_left_idx + 1: last_right_idx])

            # print("num_str: ", num_str)
            # print("ss[first_left_idx + 1: last_right_idx]: ", ss[first_left_idx + 1: last_right_idx])

            return pre_str + in_str * int(num_str) + backtrace(ss[last_right_idx + 1:])

        return backtrace(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.decodeString(s="3[a2[c]]"))
    print(solution.decodeString("3[a]2[bc]"))
    print(solution.decodeString("2[abc]3[cd]ef"))
    print(solution.decodeString("abc3[cd]xyz"))
