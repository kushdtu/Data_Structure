
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def printLL(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end='')
            temp = temp.next
        print()

    def detectLoop(self):
        slow = self.head
        fast = self.head
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.printLL()
# ll.head.next.next.next.next = ll.head.next.next
print(ll.detectLoop())


'''
Detect loop in a linked list
Given a linked list, check if the linked list has loop or not.
'''