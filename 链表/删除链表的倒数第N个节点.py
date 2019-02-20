'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

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


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if head is None:
            return n-1
        print("进入节点", head.val)
        t = self.removeNthFromEnd(head.next, n)
        if isinstance(t, ListNode) or t is None:
            head.next = t
            return head
        elif t == 0:
            print("*****删除节点*****", head.val)
            return head.next
        else:
            return t-1
        print("退出节点", p.val)

head = ListNode(1)
p = head
for i in range(2,3):
    p.next = ListNode(i)
    p = p.next
print(head)
s = Solution()
n = s.removeNthFromEnd(head,1)
print(head)



