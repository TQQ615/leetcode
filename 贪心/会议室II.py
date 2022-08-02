"""
给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，
返回 所需会议室的最小数量 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/meeting-rooms-ii

eg1:
输入：intervals = [[0,30],[5,10],[15,20]]
输出：2

eg2:
输入：intervals = [[7,10],[2,4]]
输出：1
"""
from typing import Optional, List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        begin = []
        end = []
        for k in intervals:
            begin.append(k[0])
            end.append(k[1])
        begin = sorted(begin)
        end = sorted(end)
        i = 0
        j = 0
        n = len(intervals)
        relt = 0
        count = 0
        # print('begin: ', begin)
        # print('end: ', end)
        # check时间线上是否有重合，重合的最多次数就是会议室的最小数量
        while i < n and j < n:
            if begin[i] < end[j]:
                i += 1
                count += 1
            else:
                j += 1
                count -= 1
            # print("cnt: ", count)
            relt = max(count, relt)
        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.minMeetingRooms([[0,30],[5,10],[15,20]]))
    print(solution.minMeetingRooms([[7,10],[2,4]]))

