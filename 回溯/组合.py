from typing import Optional, List

"""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。
eg1:
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


"""
元素无重不可复选，即 nums 中的元素都是唯一的，每个元素最多只能被使用一次：
/* 组合/子集问题回溯算法框架 */
void backtrack(int[] nums, int start) {
    // 回溯算法标准框架
    for (int i = start; i < nums.length; i++) {
        // 做选择
        track.addLast(nums[i]);
        // 注意参数
        backtrack(nums, i + 1);
        // 撤销选择
        track.removeLast();
    }
}
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        relt = list()

        def backtrace(demo, kk, start_idx):
            if kk == k:
                relt.append([_ for _ in demo])
            for i in range(start_idx, n + 1):
                demo.append(i)
                backtrace(demo, kk + 1, i + 1)
                demo.pop()

        backtrace([], 0, 1)
        return relt


"""
给你一个 无重复元素 的整数数组candidates 和一个目标整数target，找出candidates中可以使数字和为目标数target 的 所有不同组合 ，
并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为target 的不同组合数少于 150 个。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/combination-sum

eg1:
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。

eg2:
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]

eg3:
输入: candidates = [2], target = 1
输出: []

"""

"""
元素无重可复选，即 nums 中的元素都是唯一的，每个元素可以被使用若干次，只要删掉去重逻辑即可
/* 组合/子集问题回溯算法框架 */
void backtrack(int[] nums, int start) {
    // 回溯算法标准框架
    for (int i = start; i < nums.length; i++) {
        // 做选择
        track.addLast(nums[i]);
        // 注意参数
        backtrack(nums, i);
        // 撤销选择
        track.removeLast();
    }
}
"""


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        relt = list()

        def backtrace(relt_demo, sum_all, start_idx):
            if sum_all == target:
                if relt_demo not in relt:
                    relt.append([_ for _ in relt_demo])
            if sum_all > target:
                return
            for i in range(start_idx, len(candidates)):
                relt_demo.append(candidates[i])
                sum_all += candidates[i]
                # 从当前id开始，表示可重复，但是没必要从i=0开始，都是重复的子问题，增加计算量
                backtrace(relt_demo, sum_all, i)
                sum_all -= candidates[i]
                relt_demo.pop()

        backtrace([], 0, 0)
        return relt


"""
给定一个候选人编号的集合candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。

candidates中的每个数字在每个组合中只能使用一次。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/combination-sum-ii

eg1:
输入: candidates =[10,1,2,7,6,1,5], target =8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

eg2:
输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]

"""

"""
元素可重不可复选，即 nums 中的元素可以存在重复，每个元素最多只能被使用一次，其关键在于排序和剪枝：
Arrays.sort(nums);
/* 组合/子集问题回溯算法框架 */
void backtrack(int[] nums, int start) {
    // 回溯算法标准框架
    for (int i = start; i < nums.length; i++) {
        // 剪枝逻辑，跳过值相同的相邻树枝
        if (i > start && nums[i] == nums[i - 1]) {
            continue;
        }
        // 做选择
        track.addLast(nums[i]);
        // 注意参数
        backtrack(nums, i + 1);
        // 撤销选择
        track.removeLast();
    }
}
"""


class Solution3:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        relt = list()
        candidates = sorted(candidates)

        def backtrace(sum_all, relt_e, start_idx):
            if sum_all == target:
                if relt_e not in relt:
                    relt.append([_ for _ in relt_e])
            if sum_all > target:
                return
            for i in range(start_idx, len(candidates)):
                # 剪枝
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                sum_all += candidates[i]
                relt_e.append(candidates[i])
                backtrace(sum_all, relt_e, i + 1)
                relt_e.pop()
                sum_all -= candidates[i]
        backtrace(0, [], 0)
        return relt


"""
找出所有相加之和为n 的k个数的组合，且满足下列条件：

只使用数字1到9
每个数字最多使用一次
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/combination-sum-iii

eg1:
输入: k = 3, n = 7
输出: [[1,2,4]]
解释:
1 + 2 + 4 = 7
没有其他符合的组合了。

eg2:
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
解释:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
没有其他符合的组合了。


eg3:
输入: k = 4, n = 1
输出: []
解释: 不存在有效的组合。
在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。

"""


class Solution4:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        # target = n
        # number of number = k
        relt = list()

        def backtrace(relt_e, start_idx):
            if len(relt_e) == k and sum(relt_e) == n:
                relt.append([_ for _ in relt_e])
                return
            for i in range(start_idx, len(nums)):
                if sum(relt_e) + nums[i] > n:
                    continue
                relt_e.append(nums[i])
                backtrace(relt_e, i + 1)
                relt_e.pop()
        backtrace([], 0)
        return relt

"""
给定list a=[1,2,3], 整数m=2, 求从a中国取出m个元素的所有组合如[[1,2], [1,3], [2,3]] 

"""


def getRelt(nums, m):
    relt = list()

    def backtrace(relt_e, idx):
        if len(relt_e) == m:
            relt.append([_ for _ in relt_e])
            return
        for i in range(idx, len(nums)):
            relt_e.append(nums[i])
            backtrace(relt_e, i + 1)
            relt_e.pop()
    backtrace([], 0)
    return relt


if __name__ == '__main__':
    # solution = Solution()
    # print(solution.combine(4,2))

    # solution = Solution2()
    # print(solution.combinationSum(candidates = [2,3,6,7], target = 7))
    # print(solution.combinationSum(candidates = [2,3,5], target = 8))

    # solution = Solution3()
    # print(solution.combinationSum2(candidates =[10,1,2,7,6,1,5], target =8))
    # print(solution.combinationSum2(candidates = [2,5,2,1,2], target = 5))

    # solution = Solution4()
    # print(solution.combinationSum3(k=3, n=7))

    print(getRelt([1,2,3], 2))
