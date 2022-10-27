# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        def swap2(head):
            if head==None:
                return None
            elif head.next==None:
                return head
            
            if head!=None and head.next!= None:
                a = head
                b = head.next
                c = head.next.next

                b.next = a
                b.next.next = swap2(c)
                
                return b
                
            
        mm = swap2(head)

        return mm
