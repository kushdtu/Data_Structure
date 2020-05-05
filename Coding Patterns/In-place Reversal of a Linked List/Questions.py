
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

def printLL(head):
    temp = head
    while temp is not None:
        print(temp.data, end="->")
        temp = temp.next
    print()

def reverseLL(head):
    if head is None:
        return head
    
    prev, current, next = None, head, None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''
def reverseSubLinkedList(head, m, n):

    cur, prev = head, None
    while m > 1:
        prev = cur
        cur = cur.next
        m, n = m-1, n-1
    
    tail, con = cur, prev
    while(n > 0):
        third = cur.next
        cur.next = prev
        prev = cur
        cur = third
        n -= 1
    
    if con:
        con.next = prev
    else:
        head = prev
    tail.next = cur
    return head


ll = linkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(5)
printLL(ll.head)
# head = reverseLL(ll.head)

head = reverseSubLinkedList(ll.head, 2, 4)
printLL(head)
