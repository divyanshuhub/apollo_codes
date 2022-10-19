# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a = []
        while head!=None:
            a.append(head.val)
            head = head.next
        l = len(a)
        a.pop(l - n)
        h1 = c = ListNode(0,None)
        for i in range(l-1):
            c.next = ListNode(a[i],None)
            c = c.next
        return h1.next
