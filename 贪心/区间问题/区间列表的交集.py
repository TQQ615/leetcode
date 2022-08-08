"""
给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，
其中 firstList[i] = [starti, endi] 而secondList[j] = [startj, endj] 。
每个区间列表都是成对 不相交 的，并且 已经排序 。

返回这 两个区间列表的交集 。

形式上，闭区间[a, b]（其中a <= b）表示实数x的集合，而a <= x <= b 。

两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/interval-list-intersections

eg1:
输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

eg2:
输入：firstList = [[1,7]], secondList = [[3,10]]
输出：[[3,7]]

eg3:
输入：firstList = [[1,3],[5,9]], secondList = []
输出：[]
"""
from typing import Optional, List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n1 = len(firstList)
        n2 = len(secondList)
        i = 0
        j = 0
        relt = []

        while i < n1 and j < n2:
            a1 = firstList[i][0]
            a2 = firstList[i][1]

            b1 = secondList[j][0]
            b2 = secondList[j][1]

            # if a1 > b2:
            #     j += 1
            # elif b1 > a2:
            #     i += 1
            # elif b2 > a2:
            #     relt.append([max(a1, b1), a2])
            #     i += 1
            # elif b2 < a2:
            #     relt.append([max(a1, b1), b2])
            #     j += 1
            if b2 >= a1 and a2 >= b1:
                relt.append([max(a1, b1), min(a2, b2)])
            if b2 < a2:
                j += 1
            else:
                i += 1
        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]],
                                        secondList = [[1,5],[8,12],[15,24],[25,26]]))
