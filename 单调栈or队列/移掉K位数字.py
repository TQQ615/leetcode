"""
给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。

eg1:
输入：num = "1432219", k = 3
输出："1219"
解释：移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。

eg2:
输入：num = "10200", k = 1
输出："200"
解释：移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。

eg3:
输入：num = "10", k = 2
输出："0"
解释：从原数字移除所有的数字，剩余为空就是 0 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/remove-k-digits
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        stack = []
        delete_num = 0
        # 给定一个长度为 nn 的数字序列 [D_0, D_1, D_2, D_3 ..., D_{n-1}]，从左往右找到第一个位置 i（i>0）使得 D_i<D_{i-1}，
        # 并删去 D_{i-1}；如果不存在，说明整个数字序列单调不降，删去最后一个数字即可。
        for i in range(n):
            while len(stack) > 0 and stack[-1] > num[i] and delete_num < k:
                delete_num += 1
                stack.pop()
            stack.append(num[i])
        # 序列基本递增，没有删除够，直接删掉最后 k - delete_num 个
        if delete_num < k:
            stack = stack[: -(k - delete_num)]
        # 如果开头是 0 则需要去掉
        while len(stack) > 0 and stack[0] == '0':
            stack.pop(0)
        # 如果删光了，结果是0
        return "".join(stack) if len(stack) > 0 else '0'


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeKdigits(num = "1432219", k = 3))
    print(solution.removeKdigits(num = "10200", k = 1))
    print(solution.removeKdigits(num = "10", k = 2))
    print(solution.removeKdigits(num = "9", k = 1))


