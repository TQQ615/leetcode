"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
eg1:
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        reversed_head = self.reverseList(head.next)
        p = reversed_head
        while p.next is not None:
            p = p.next
        p.next = head
        head.next = None
        return reversed_head

    # 非递归
    def reverseList2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p = head
        reversed_head = head
        q = head
        while p is not None:
            p = p.next
            q.next = reversed_head
            reversed_head = q
            q = p
        head.next = None

        return reversed_head

"""
反转链表前 N 个节点

"""


class Solution2:
    def __init__(self):
        self.successor = None

    # def reverseN(self, head: ListNode, n: int) -> ListNode:
    #     if n == 1 or head is None or head.next is None:
    #         return head
    #     reversed_head_n_1 = self.reverseN(head.next, n - 1)
    #     p = reversed_head_n_1
    #     for i in range(n - 2):
    #         p = p.next
    #     head.next = p.next
    #     p.next = head
    #     return reversed_head_n_1

    def reverseN2(self, head: ListNode, n: int) -> ListNode:
        if n == 1:
            self.successor = head.next
            return head
        reversed_head_n_1 = self.reverseN2(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return reversed_head_n_1

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == 1:
            return self.reverseN2(head, right)
        reversed_last = self.reverseBetween(head.next, left - 1, right - 1)
        head.next = reversed_last
        return head



"""
给你单链表的头指针 head 和两个整数left 和 right ，其中left <= right 。
请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-linked-list-ii

eg1:
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
"""


class Solution3:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # TODO 见solution2
        return head


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    hh = solution.reverseList2(head)
    # hh = solution.reverseN2(head, 2)
    # hh = solution.reverseBetween(head, 2, 4)
    pp = hh
    while pp is not None:
        print(pp.val)
        pp = pp.next
