"""
给定一个长度为n的链表head

对于列表中的每个节点，查找下一个 更大节点 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 严格大于 它的值。

返回一个整数数组 answer ，其中 answer[i] 是第 i 个节点( 从1开始 )的下一个更大的节点的值。
如果第 i 个节点没有下一个更大的节点，设置answer[i] = 0。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/next-greater-node-in-linked-list

eg1:
输入：head = [2,1,5]
输出：[5,5,0]

eg2:
输入：head = [2,7,4,3,5]
输出：[7,0,5,5,0]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
        n = len(nums)
        stack = []
        relt = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and stack[-1] <= nums[i]:
                stack.pop()
            relt[i] = stack[-1] if len(stack) > 0 else 0
            stack.append(nums[i])
        return relt