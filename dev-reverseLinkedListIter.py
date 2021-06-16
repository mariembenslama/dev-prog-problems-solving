class LinkedList:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    global reversedLinkedListIter
    def reversedLinkedListIter(head:LinkedList) -> LinkedList:
        prev = None
        curr = head
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
    
    def test(head): 
        head = reversedLinkedListIter(head) 
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

    