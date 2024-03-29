"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

eg1:
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

eg2:
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
from typing import Optional, List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        relt = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] > relt[-1][1]:
                relt.append(intervals[i])
            elif intervals[i][1] > relt[-1][1]:
                relt[-1][1] = intervals[i][1]
        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(solution.merge([[1,4],[4,5]]))