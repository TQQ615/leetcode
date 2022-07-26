"""
给定一个整数数组temperatures，表示每天的温度，返回一个数组answer，其中answer[i]是指对于第 i 天，下一个更高温度出现在几天后。
如果气温在这之后都不会升高，请在该位置用0 来代替。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/daily-temperatures

eg1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

eg2:
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]

eg3:
输入: temperatures = [30,60,90]
输出: [1,1,0]
"""
from typing import Optional, List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        # relt = []
        relt = [0 for _ in range(n)]

        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if len(stack) > 0:
                relt[i] = stack[-1] - i
            stack.append(i)
        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.dailyTemperatures([30,60,90]))
    print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))

