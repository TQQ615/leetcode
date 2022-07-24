"""
给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。

已知存在楼层 f ，满足0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。

每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足1 <= x <= n）。
如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。

请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/super-egg-drop

eg1:
输入：k = 1, n = 2
输出：2
解释：鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。
    否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。
    如果它没碎，那么肯定能得出 f = 2 。
    因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。

eg2:
输入：k = 2, n = 6
输出：3

eg3:
输入：k = 3, n = 14
输出：4

注意：
1 <= k <= 100
1 <= n <= 104
"""


class Solution:
    # 超时 O(KN^2)
    def superEggDrop1(self, k: int, n: int) -> int:
        # dp状态矩阵：dp[i][j]表示用i + 1个鸡蛋测试j个楼层，最坏的情况下的最少操作数
        dp = [[0 for _ in range(n + 1)] for _ in range(k)]

        # 只有一个鸡蛋(i + 1 == 1)时，最少操作数是楼层数
        for j in range(n + 1):
            dp[0][j] = j
        # 只有0层(j == 0)时，最少操作数是0
        for i in range(k):
            dp[i][0] = 0

        for i in range(1, k):
            for j in range(1, n + 1):
                # 找最小操作数，先初始化为最大的
                dp[i][j] = 10000000000
                # 结果是否在第j层扔鸡蛋中找最小
                for k in range(1, j + 1):
                    dp[i][j] = min(dp[i][j],
                                   # 找最坏的情况，对应的dp值，就是最坏情况的最小操作数
                                   max(
                                       # 鸡蛋碎了，用剩下的 (i + 1) - 1 个鸡蛋测试下面 1 ~ (k - 1) 层
                                       dp[i - 1][k - 1],
                                       # 鸡蛋没碎，还有(i + 1)个鸡蛋，测试上面 (k + 1) ~ j层，等价于测试 1 ~ (j - k)
                                       dp[i][j - k]
                                   ) + 1
                                   )
        # print('dp: ', dp)
        return dp[-1][-1]

    # 超时 O(KN^2)
    def superEggDrop2(self, k: int, n: int) -> int:
        mome = dict()

        def dp(kk, nn):
            if kk == 1:
                return nn
            if nn == 0:
                return 0
            if (kk, nn) in mome.keys():
                return mome.get((kk, nn))

            res = float("inf")
            for i in range(1, nn + 1):
                res = min(
                    res,
                    max(
                        # 鸡蛋没碎，仍有kk个鸡蛋，往1~(i - 1)找
                        dp(kk, i - 1),
                        # 鸡蛋碎了，只有kk - 1个鸡蛋，往(i+1) ~ nn层找
                        dp(kk - 1, nn - i)
                    ) + 1
                )
            mome[(kk, nn)] = res
            return res

        return dp(k, n)

    # 二分搜索的优化
    # dp[i][j]关于j是单调函数，可以用二分法求解
    # O(KNlogN)
    def superEggDrop3(self, k: int, n: int) -> int:
        mome = dict()

        def dp(kk, nn):
            if kk == 1:
                return nn
            if nn == 0:
                return 0
            if (kk, nn) in mome.keys():
                return mome[(kk, nn)]

            left = 1
            right = nn
            res = 100000000000
            while left <= right:
                mid = left + (right - left) // 2
                broken = dp(kk - 1, mid - 1)
                not_broken = dp(kk, nn - mid)
                if broken > not_broken:
                    right = mid - 1
                    res = min(res, broken + 1)
                if broken < not_broken:
                    left = mid + 1
                    res = min(res, not_broken + 1)
                if broken == not_broken:
                    left = mid + 1
                    res = min(res, broken + 1)
            mome[(kk, nn)] = res
            return res

        return dp(k, n)

    # 重新定义dp[i][j]: 用i个鸡蛋，最多测试j次，可以确定的最高楼层
    # O(KN)
    def superEggDrop4(self, k: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

        # 用0个鸡蛋，只能确定0层：dp[0][j] = 0
        # 用1个鸡蛋，最多测试j次，最高可以确定j层
        for j in range(1, n + 1):
            dp[1][j] = j
        # 最多只能测试1次，最高可以确定的楼层是1
        for i in range(1, k + 1):
            dp[i][1] = 1

        j = 1
        while dp[k][j] < n:
            j += 1
            for i in range(2, k + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1] + 1
                # 鸡蛋没碎的最高楼层 + 鸡蛋碎了的最高楼层 + 当前楼层被测试过了
        return j

    # 空间优化：
    # 时间：O(KN)，空间：O(K)
    def superEggDrop5(self, k: int, n: int) -> int:
        # dp[i] 表示：用i个鸡蛋，当前最多测试步数（此时是1）时，可以测试出的最高楼层
        dp = [0] + [1 for _ in range(k)]

        j = 1
        while dp[k] < n:
            j += 1
            # 依赖上一步的 i - 1 哥鸡蛋的结果，所以需要从后往前更新
            for i in range(k, 0, -1):
                dp[i] = dp[i] + dp[i - 1] + 1
        return j

    # 时间优化，dp[i][j]: 使用i个鸡蛋，测试j步，最多可以确定多少层
    # dp[i][j] 关于j是单调递增函数，可使用二分法简化时间复杂度
    # 时间：O(KlogN)
    # TODO 关于j的递增函数，每一步依赖前一步的计算，how to 二分法？？？？
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
        # 对于i = 0，只有0个鸡蛋，只能确定0层：dp[0][j] = 0
        # 对于j = 0, 只有0步，只能确定0层：dp[i][j] = 0

        j = 0
        while dp[k][j] < n:
            j += 1
            for i in range(1, k + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1] + 1
            # print('i:', i, ' j: ', j, ' dp[i][j]:', dp[i][j])
        return j


if __name__ == '__main__':
    solution = Solution()
    print(solution.superEggDrop(k=1, n=2))
    print(solution.superEggDrop(k=2, n=6))
    print(solution.superEggDrop(k=3, n=14))
    print(solution.superEggDrop(k=4, n=5000))
