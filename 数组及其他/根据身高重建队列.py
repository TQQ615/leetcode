"""

"""
from typing import Optional, List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        people.sort(key=lambda x: (-x[0], x[1]))
        relt = []
        for i in range(n):
            idx = people[i][1]
            relt = relt[:idx] + [people[i]] + relt[idx:]
        return relt


if __name__ == '__main__':
    solution = Solution()
    print(solution.reconstructQueue(people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
