"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

eg1:
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/merge-k-sorted-lists。
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 分而治之，两两合并，再全部合并
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(list1, list2):
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

        def backtrace(lists):
            n = len(lists)
            if n == 1:
                return lists[0]
            if n == 0:
                return None
            mid = int(n / 2)
            left = backtrace(lists[:mid])
            right = backtrace(lists[mid:])
            return merge2Lists(left, right)

        return backtrace(lists)


# 建立最小堆，每次取堆顶的元素合并到新的链表
class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ll = []
        for i in range(len(lists)):
            if lists[i] is not None:
                ll.append(lists[i])
        lists = ll
        k = len(lists)
        if k == 1:
            return lists[0]
        if k == 0:
            return None
        list_len = k

        def heapify(lists, root):
            left = 2 * root + 1
            right = 2 * root + 2
            ori_root = root
            if left < list_len and lists[left].val < lists[root].val:
                root = left
            if right < list_len and lists[right].val < lists[root].val:
                root = right
            if root != ori_root:
                lists[root], lists[ori_root] = lists[ori_root], lists[root]
                heapify(lists, root)

        def buildHeap(lists):
            for i in range(len(lists) - 1, -1, -1):
                heapify(lists, i)

        buildHeap(lists)
        head = ListNode(-1, None)
        p = head

        while len(lists) > 0:
            p.next = lists[0]
            p = p.next
            if lists[0].next is None:
                if len(lists) > 1:
                    lists[0] = lists[-1]
                    list_len -= 1
                lists.pop()
            else:
                lists[0] = lists[0].next
            if len(lists) > 0 and lists[0] is not None:
                heapify(lists, 0)

        return head.next


if __name__ == '__main__':
    solution = Solution2()
    lists = list()
    # lists.append(ListNode(1, ListNode(2, ListNode(3))))
    # lists.append(ListNode(2, ListNode(3, ListNode(4))))
    # lists.append(ListNode(3, ListNode(4, ListNode(5))))
    # lists.append(None)
    # lists.append(None)
    # lists.append(ListNode(1))
    # lists.append(ListNode(0))
    hh = solution.mergeKLists([None for _ in range(10)])
    pp = hh
    while pp is not None:
        print(pp.val)
        pp = pp.next
