"""
0-1背包问题：
给你一个可装载重量为 W 的背包和 N 个物品，
每个物品有重量和价值两个属性。
其中第 i 个物品的重量为 wt[i]，价值为 val[i]，现在让你用这个背包装物品，最多能装的价值是多少？
eg1:
N = 3, W = 4
wt = [2, 1, 3]
val = [4, 2, 3]
"""


def getRelt(N, W, wt, val):
    # dp[w][n]：可装重量为w，n个物品的背包，可装的最大价值是多少
    dp = [[0 for _ in range(N + 1)] for _ in range(W + 1)]
    # 对于 n = 0，最大价值是0，对于w = 0，最大价值也是0
    for i in range(1, W + 1):
        for j in range(1, N + 1):
            # 第j个物品的重量大于总重量
            if wt[j - 1] > i:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = max(
                    # 选择当前第j个物品
                    dp[i - wt[j - 1]][j - 1] + val[j - 1],
                    # 不选择当前第j个物品
                    dp[i][j - 1]
                )
    return dp[W][N]


N = 3
W = 4
wt = [2, 1, 2]
val = [4, 2, 3]
print(getRelt(N, W, wt, val))