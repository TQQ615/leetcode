"""
给定一个区间的集合intervals，其中 intervals[i] = [starti, endi]。返回 需要移除区间的最小数量，使剩余区间互不重叠。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/non-overlapping-intervals

eg1:
输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。

eg2:
输入: intervals = [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
"""
from typing import Optional, List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        # print(intervals)
        relt = 1
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= right:
                right = intervals[i][1]
                relt += 1

        return len(intervals) - relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))
    print(solution.eraseOverlapIntervals(intervals = [ [1,2], [1,2], [1,2] ]))
