"""
给你链表的头节点 head ，每k个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-nodes-in-k-group

eg1:
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]

eg2:
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.successor = None

    def reserve(self, head):
        if head is None or head.next is None:
            return head
        last = self.reserve(head.next)
        head.next.next = head
        head.next = None
        return last

    def reserveN(self, head, n):
        if n == 1:
            self.successor = head.next
            return head
        last = self.reserveN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = head
        b = head
        for i in range(k):
            if b is None:
                return head
            b = b.next
        reversed_last = self.reverseKGroup(b, k)
        reversed_a = self.reserveN(a, k)
        head.next = reversed_last
        return reversed_a


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    hh = solution.reverseKGroup(head, 5)
    pp = hh
    while pp is not None:
        print(pp.val)
        pp = pp.next