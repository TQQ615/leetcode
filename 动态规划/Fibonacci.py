"""
斐波那契数（通常用F(n) 表示）形成的序列称为 斐波那契数列 。该数列由0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定n ，请计算 F(n) 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/fibonacci-number
"""


# 递归：时间复杂度O(2^n)
# 问题：重叠子问题：重复计算
class Solution1(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in (0, 1):
            return n
        return self.fib(n - 1) + self.fib(n - 2)


# 带备忘录的递归解法
# 时间复杂度O(n)
class Solution2(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic = dict()

        def helper(n):
            if n in dic.keys():
                return dic
            if n in (0, 1):
                return n
            return helper(n - 1) + helper(n - 2)
        return helper(n)


# 动态规划解法
# 时间复杂度O(n)
# 空间复杂度O(n)
# 状态转移方程: f(n) = n, n<=1; f(n) = f(n-1) + f(n-2), n>1;
class Solution3(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        ll = list()
        ll.append(0)
        ll.append(1)
        for i in range(2, n + 1):
            ll.append(ll[i - 1] + ll[i - 2])
        return ll[n]


class Solution4(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in (0, 1):
            return n
        pre = 0
        curr = 1
        for i in range(2, n + 1):
            relt = pre + curr
            pre = curr
            curr = relt
        return curr


if __name__ == '__main__':
    solution = Solution4()
    print(solution.fib(5))
