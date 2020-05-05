
# Flatten a multilevel linked list
'''
Given a linked list where in addition to the next pointer, each node has a child 
pointer, which may or may not point to a separate list. These child lists may have
one or more children of their own, and so on, to produce a multilevel 
data structure, as shown in below figure.You are given the head of the first level 
of the list. Flatten the list so that all the nodes appear in a single-level 
linked list. You need to flatten the list in way that all nodes at first level 
should come first, then nodes of second level, and so on.
'''
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None
		self.child = None

# Return Node 
def newNode(data): 
	return Node(data) 

def flattenlist(head):
    # Base case
    if head is None:
        return

    tail = head
    while(tail.next != None):
        tail = tail.next
    current = head

    while(current != tail):

        if(current.child):
            tail.next = current.child

            temp = current.child
            while(temp.next):
                temp = temp.next
            tail = temp
        
        current = current.next
    return head


# A utility function to print 
# all nodes of a linked list 
def printList(head): 
	if not head: 
		return
	while(head): 
		print(head.data, end = "->") 
		head = head.next

	
# Child list of 13 
child13 = newNode(16) 
child13.child = newNode(3) 

# Child List of 10 
head1 = newNode(4) 
head1.next = newNode(20) 
head1.next.child = newNode(2) #Child of 20 
head1.next.next = newNode(13) 
head1.next.next.child = child13 

# Child of 9 
child9 = newNode(19) 
child9.next = newNode(15) 

# Child List of 17 
child17 = newNode(9) 
child17.next = newNode(8) 
child17.child = child9 

# Child List of 7 
head2 = newNode(17) 
head2.next = newNode(6) 
head2.child = child17 

# Main List 
head = newNode(10) 
head.child = head1 
head.next = newNode(5) 
head.next.next = newNode(12) 
head.next.next.next = newNode(7) 
head.next.next.next.child = head2 
head.next.next.next.next = newNode(11) 

flattenlist(head)
printList(head)
print()
