'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

'''


# Definition for singly-linked list.
class ListNode:
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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        now = ListNode(head.val)
        head = head.next
        while head is not None:
            p = ListNode(head.val)
            p.next = now
            now = p
            head = head.next

        return now

head = ListNode(1)
p = head
for i in range(2,6):
    p.next = ListNode(i)
    p = p.next
print(head)
s = Solution()
now = s.reverseList(head)
print(now)