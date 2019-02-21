'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = ""
        while self != None:
            s = s+str(self.val)+"-->"
            self = self.next
        return s

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        p = head
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
        if l1 is not None:
            p.next = l1
        if l2 is not None:
            p.next = l2

        return head.next

head = ListNode(1)
head2 = ListNode(1)
p,q = head,head2
for i in range(2,6):
    p.next = ListNode(i)
    q.next = ListNode(i)
    p = p.next
    q = q.next
print(head,head2)
s = Solution()
now = s.mergeTwoLists(None,None)
print(now)
