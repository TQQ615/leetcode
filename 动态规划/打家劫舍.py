"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/house-robber

eg1:
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
   偷窃到的最高金额 = 1 + 3 = 4 。

eg2:
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
    偷窃到的最高金额 = 2 + 9 + 1 = 12 。

"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) < 3:
        #     return max(nums)
        # # 不抢
        # dp_i_0 = 0
        # # 抢
        # dp_i_1 = 0
        # final = 0
        # # 注意这里从最后一个房子开始计算，原因是越靠后越是子问题？
        # for i in range(len(nums) - 1, -1, -1):
        #     final = max(dp_i_0 + nums[i], dp_i_1)
        #     dp_i_0 = dp_i_1
        #     dp_i_1 = final
        # return final

        if len(nums) < 3:
            return max(nums)
        # 截止第0个房子的最大收益
        dp0 = nums[0]
        # 截止第1个房子的最大收益: 此时第1个房子被抢或没有被抢的情况都被考虑进去了
        dp1 = max(nums[0], nums[1])
        final = 0
        for i in range(2, len(nums)):
            # dp[0] + nums[i]: 第i个房子被抢，只能从i-2个房子的最大收益继续，因为被抢这一行为不可能从第i-1个房子开始
            # dp1: 第i个房子没被抢，从第i-1个房子被抢or没被抢的情况继续，包含连续不被抢的情况
            final = max(dp0 + nums[i], dp1)
            dp0 = dp1
            dp1 = final
        return final


# 首尾两两间房子相连，不能同时抢
class Solution2(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def rob_base(nums):
            if len(nums) < 3:
                return max(nums)

            dp0 = nums[0]
            dp1 = max(nums[0], nums[1])
            final = 0
            for i in range(2, len(nums)):
                final = max(dp0 + nums[i], dp1)
                dp0 = dp1
                dp1 = final
            return final

        return max(rob_base(nums[1:]), rob_base(nums[:-1]))


"""
小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为root。

除了root之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，
聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

给定二叉树的root。返回在不触动警报的情况下，小偷能够盗取的最高金额。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/house-robber-iii

eg1:
输入: root = [3,2,3,null,3,null,1]
输出: 7 
解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7

eg2:
输入: root = [3,4,5,1,3,null,1]
输出: 9
解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution3(object):
    sub_pro = dict()

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        # 不抢
        dp0 = self.rob(root.left) + self.rob(root.right)
        # 抢
        dp1 = root.val + (0 if root.left is None else self.rob(root.left.left) + self.rob(root.left.right)) \
              + (0 if root.right is None else self.rob(root.right.left) + self.rob(root.right.right))
        relt = max(dp0, dp1)
        return relt

        # def base(root):
        #     if root is None:
        #         return 0, 0
        #     left_dp = base(root.left)
        #     right_dp = base(root.right)
        #     rob_it = root.val + left_dp[0] + right_dp[0]
        #     # not_rob的解释：
        #     # 根节点不偷时左子树能带来的最大收益（左子树可偷可不偷）
        #     # 根节点不偷时右子树能带来的最大收益（右子树可偷可不偷）
        #     return max(left_dp[0], left_dp[1]) + max(right_dp[0], right_dp[1]), rob_it
        # return max(base(root)[0], base(root)[1])


if __name__ == '__main__':
    # solution = Solution()
    # print(solution.rob([200,3,140,20]))
    # solution = Solution2()
    # print(solution.rob([200, 3, 140, 20, 10]))
    solution = Solution3()
    # root = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3))
    # badcase: root = [3,2,3,null,3,null,1]
    root = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
    print(solution.rob(root))
