"""
有 n 个城市通过一些航班连接。给你一个数组
flights ，其中flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格 pricei 抵达 toi。

现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k站中转的路线，
使得从 src 到 dst 的 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/cheapest-flights-within-k-stops

eg1:
输入:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
输出: 200

eg2:
输入:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
输出: 500

"""
from typing import Optional, List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dp[i][j]: 表示从src出发j次中转可以到达i点的最便宜的机票选择
        dp = [[1000000 for _ in range(k + 1)] for _ in range(n)]
        # 价格table
        price = [[-1 for _ in range(n)] for _ in range(n)]
        for f in flights:
            from_city = f[0]
            to_city = f[1]
            price_ = f[2]
            price[from_city][to_city] = price_
        # print('price: ', price)
        # 中转0次就是直达：
        for i in range(n):
            if price[src][i] > 0:
                dp[i][0] = price[src][i]
        # 任何中转次数，目的地是src的时候，最便宜的机票选择是0
        for kk in range(k + 1):
            dp[src][kk] = 0
            # print('i:', i, 'dp[i][0]: ', dp[i][0])

        for kk in range(1, k + 1):
            # to j city
            for j in range(n):
                # from i city
                for i in range(n):
                    if price[i][j] >= 0:
                        dp[j][kk] = min(dp[j][kk], dp[i][kk - 1] + price[i][j])
                # print('j:', j, ' kk:', kk, 'dp[j][kk]: ', dp[j][kk])
        return dp[dst][k] if dp[dst][k] != 1000000 else -1


if __name__ == '__main__':
    solution = Solution()
    # print(solution.findCheapestPrice(n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=1))
    # print(solution.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0))
    # print(solution.findCheapestPrice(3, [[0,1,2],[1,2,1],[2,0,10]], 1, 2, 1))
    print(solution.findCheapestPrice(10, [[3,4,4],[2,5,6],[4,7,10],
                                          [9,6,5],[7,4,4],[6,2,10],
                                          [6,8,6],[7,9,4],[1,5,4],
                                          [1,0,4],[9,7,3],[7,0,5],
                                          [6,5,8],[1,7,6],[4,0,9],
                                          [5,9,1],[8,7,3],[1,2,6],
                                          [4,1,5],[5,2,4],[1,9,1],
                                          [7,8,10],[0,4,2],[7,2,8]], 6, 0, 7))








