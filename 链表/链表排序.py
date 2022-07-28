"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

eg1:
输入：head = [4,2,1,3]
输出：[1,2,3,4]

eg2:
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(head1, head2):
            hh = ListNode()
            p = head1
            q = head2
            h = hh
            while p is not None and q is not None:
                if p.val < q.val:
                    h.next = p
                    p = p.next
                else:
                    h.next = q
                    q = q.next
                h = h.next
            if p is not None:
                h.next = p
            if q is not None:
                h.next = q
            return hh.next

        def traceback(ll):
            if ll is None or ll.next is None:
                return ll
            fast = ll
            slow = ll
            slow_prev = ListNode(-1, ll)
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow_prev = slow_prev.next
                slow = slow.next
            slow_prev.next = None
            # print('ll')
            # printList(ll)
            # print('slow')
            # printList(slow)
            return merge(traceback(ll), traceback(slow))

        return traceback(head)


def printList(hh):
    pp = hh
    while pp is not None:
        print(pp.val)
        pp = pp.next


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    hh = solution.sortList(head)
    printList(hh)
