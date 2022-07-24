"""
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

eg1:
输入：head = [1,2,2,1]
输出：true

eg2:
输入：head = [1,2]
输出：false
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        # 快慢指针
        fast = head
        low = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            low = low.next
        # 反转后半段链表
        head2 = low.next
        reversed_head2 = ListNode(-1)
        p = head2
        q = head2
        while p is not None:
            p = p.next
            q.next = reversed_head2.next
            reversed_head2.next = q
            q = p
        # 判断反转后半段 和 前半段 是否一致
        pp = reversed_head2.next
        qq = head
        while pp is not None:
            if pp.val != qq.val:
                return False
            pp = pp.next
            qq = qq.next
        return True


if __name__ == '__main__':
    solution = Solution()
    # ll = ListNode(1, ListNode(2, ListNode(2, ListNode(2))))
    # ll = ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(1)))))
    ll = ListNode(0, ListNode(0))
    # ll = ListNode(1, ListNode(0, ListNode(0)))
    print(solution.isPalindrome(ll))
