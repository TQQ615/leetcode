"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
eg1:
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        q = head

        for i in range(n + 1):
            if p is None:
                if i == n:
                    return head.next
                else:
                    return head
            p = p.next
        while p is not None:
            p = p.next
            q = q.next
        q.next = q.next.next
        return head


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    hh = solution.removeNthFromEnd(head, 6)
    pp = hh
    while pp is not None:
        print(pp.val)
        pp = pp.next
