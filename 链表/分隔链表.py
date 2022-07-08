"""
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/partition-list

eg1:
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left = ListNode(-1, None)
        right = ListNode(-1, None)
        p = left
        q = right
        m = head
        while m is not None:
            if m.val < x:
                p.next = m
                p = p.next
            else:
                q.next = m
                q = q.next
            m = m.next

        p.next = right.next
        q.next = None
        return left.next
