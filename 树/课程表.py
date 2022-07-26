"""
你这个学期必须选修 numCourses 门课程，记为0到numCourses - 1 。

在选修某些课程之前需要一些先修课程。
先修课程按数组prerequisites 给出，其中prerequisites[i] = [ai, bi] ，表示如果要学习课程ai 则 必须 先学习课程 bi 。

例如，先修课程对[0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/course-schedule

eg1:
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。

eg2:
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。

"""
from typing import Optional, List


class Solution:
    def __init__(self):
        self.has_cycle = False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 依赖关系矩阵, dp[i][j]表示学习课程i需要依赖课程j
        dp = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        used = [0 for _ in range(numCourses)]
        # 记录已经走过的节点，后面结果是一致的
        pathed_i = [0 for _ in range(numCourses)]

        for path in prerequisites:
            dp[path[0]][path[1]] = 1

        def traverse(i):
            if used[i] == 1:
                self.has_cycle = True
                return
            if pathed_i[i] == 1 or self.has_cycle is True:
                return

            used[i] = 1
            pathed_i[i] = 1
            for j in range(numCourses):
                if dp[i][j] > 0:
                    traverse(j)
            used[i] = 0

        for i in range(numCourses):
            traverse(i)
        # print('self.has_cycle: ', self.has_cycle)
        return self.has_cycle is False


if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(numCourses = 2, prerequisites = [[1,0]]))
    print(solution.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))