class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def add(self, node):
        if self.head.value == None:
            self.head = node
        else:
            i = self.head
            while i.next != None:
                i = i.next
            i.next = node

    def printList(self):
        i = self.head
        while i != None:
            print(i.value)
            i = i.next
        '''
        if self.head == None:
            print(self.head.value)
        else:
            i = self.head
            while i != None:
                print(i.value)
                i = i.next'''

l = LinkedList()
l.printList()
n1 = Node(1)
n2 = Node(12)
n3 = Node(13)
n4 = Node(14)
n5 = Node(15)
l.add(n1)
l.add(n2)
l.add(n3)
l.add(n4)
l.add(n5)
l.printList()
