# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            c = lx = ListNode()
            while l1 and l2:
                if l1.val<l2.val:
                    #lx.next = None
                    c.next = l1
                    l1,c = l1.next,l1
                else:
                    c.next = l2
                    l2,c = l2.next,l2
                #c = c.next
            if l1 or l2:
                c.next = l1 if l1 else l2
            #print(c)
            #print(lx.next)
            return lx.next
        '''a=[]
        for i in lists:
            while i!=None:
                a.append(i.val)
                i = i.next
        a.sort()
        b=c=ListNode()
        for i in a:
            c.next = ListNode(i)
            c = c.next
        print(a)
        print(b.next)
        print(c)
        return b.next
    
        '''
        x = len(lists)
        a = ListNode()
        a = a.next
        for i in lists:
            #print("i=",i)
            if i==None:
                continue
            else:
                a = mergeTwoLists(a,i)
                #print(a)
        #print(a)
        return a
            
            
            
