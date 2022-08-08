"""
给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。

只有当c <= a且b <= d时，我们才认为区间[a,b) 被区间[c,d) 覆盖。

在完成所有删除操作后，请你返回列表中剩余区间的数目。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/remove-covered-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

eg1:
输入：intervals = [[1,4],[3,6],[2,8]]
输出：2
解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。
"""
from typing import Optional, List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        left = intervals[0][0]
        right = intervals[0][1]

        relt = 0
        for i in range(1, len(intervals)):
            # 情况一，找到覆盖区间
            if left <= intervals[i][0] and right >= intervals[i][1]:
                relt += 1
            # 情况二，找到相交区间，合并
            if intervals[i][0] < right < intervals[i][1]:
                right = intervals[i][1]
            # 情况三，完全不相交，更新起点和终点
            if intervals[i][0] > left:
                left = intervals[i][0]
                right = intervals[i][1]
        return len(intervals) - relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeCoveredIntervals([[1,4],[3,6],[2,8]]))

