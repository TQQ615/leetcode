"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/add-two-numbers

"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = l1
        q = l2
        relt = ListNode(-1)
        k = relt

        pre = 0
        while p is not None and q is not None:
            x = p.val + q.val + pre
            pre = x // 10
            k.next = ListNode(x % 10)
            k = k.next
            p = p.next
            q = q.next
        while p is not None:
            x = p.val + pre
            pre = x // 10
            k.next = ListNode(x % 10)
            k = k.next
            p = p.next
        while q is not None:
            x = q.val + pre
            pre = x // 10
            k.next = ListNode(x % 10)
            k = k.next
            q = q.next
        if pre > 0:
            k.next = ListNode(pre)
        return relt.next


if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    hh = solution.addTwoNumbers(l1, l2)
    pp = hh
    while pp is not None:
        print(pp.val)
        pp = pp.next



