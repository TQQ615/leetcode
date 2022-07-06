from typing import Optional, List

"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
eg1:
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

"""
/* 排列问题回溯算法框架 */
void backtrack(int[] nums) {
    for (int i = 0; i < nums.length; i++) {
        // 剪枝逻辑
        if (used[i]) {
            continue;
        }
        // 做选择
        used[i] = true;
        track.addLast(nums[i]);

        backtrack(nums);
        // 撤销选择
        track.removeLast();
        used[i] = false;
    }
}
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        relt = list()
        used = list()

        def backtrace(relt_e, used):
            if len(used) == len(nums):
                relt.append([_ for _ in relt_e])
            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                relt_e.append(nums[i])
                used.append(nums[i])
                backtrace(relt_e, used)
                relt_e.pop()
                used.pop()
        backtrace([], [])
        return relt


"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

eg1:
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
 
"""

"""
Arrays.sort(nums);
/* 排列问题回溯算法框架 */
void backtrack(int[] nums) {
    for (int i = 0; i < nums.length; i++) {
        // 剪枝逻辑
        if (used[i]) {
            continue;
        }
        // 剪枝逻辑，固定相同的元素在排列中的相对位置
        if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
            continue;
        }
        // 做选择
        used[i] = true;
        track.addLast(nums[i]);

        backtrack(nums);
        // 撤销选择
        track.removeLast();
        used[i] = false;
    }
}
"""


class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        relt = list()
        used = [0 for _ in range(len(nums))]

        def backtrace(relt_e, used):
            if sum(used) == len(nums):
                relt.append([_ for _ in relt_e])
            for i in range(len(nums)):
                if used[i] == 1:
                    continue
                # 剪枝逻辑，相同的元素，较后面的元素先加入relt_e时，再加入较前面的同样元素，则会有重复计算
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == 0:
                    continue
                relt_e.append(nums[i])
                used[i] = 1
                backtrace(relt_e, used)
                used[i] = 0
                relt_e.pop()
        backtrace([], used)
        return relt


if __name__ == '__main__':
    # solution = Solution()
    # print(solution.permute(nums = [1,2,3]))

    solution = Solution2()
    print(solution.permuteUnique(nums=[1,1,2]))