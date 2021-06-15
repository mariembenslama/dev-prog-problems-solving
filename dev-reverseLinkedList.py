class LinkedList:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    global reversedLinkedList
    def reversedLinkedList(head:LinkedList) -> LinkedList:
        if head is None or head.next is None:
            return head
        
        p = reversedLinkedList(head.next)
        head.next.next = head
        head.next = None
        return p
    
    def test(head): 
        head = reversedLinkedList(head) 
        while head:
            print(head.val)
            head = head.next

    # change here
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(5)
        
    test(head)

    