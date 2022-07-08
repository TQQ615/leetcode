"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
eg1:
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = list1
        q = list2
        head = ListNode(-1, None)
        d = head
        while (p is not None) and (q is not None):
            if p.val < q.val:
                d.next = p
                p = p.next
            else:
                d.next = q
                q = q.next
            d = d.next
        if p is not None:
            d.next = p
        if q is not None:
            d.next = q
        return head.next
