
# Python program to print nodes at distance k from a given node 

# A binary tree node 
class Node: 
	# A constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def printKDistanceNodeDown(root, k):
    if root is None or k < 0:
        return

    if k == 0:
        print(root.data, end=" ")
        return
    printKDistanceNodeDown(root.left, k-1)
    printKDistanceNodeDown(root.right, k-1)

def printKDistanceNodes(root, target, k):
    # Base Case 1
    if root is None:
        return -1

    if root == target:
        printKDistanceNodeDown(root, k)
        return 0

    dl = printKDistanceNodes(root.left, target, k)
    if dl != -1:

        if dl + 1 == k:
            print(root.data, end=" ")
        else:
            printKDistanceNodeDown(root.right, k-dl-2)
        
        return 1 + dl

    dr = printKDistanceNodes(root.right, target, k)
    if dr != -1:

        if dr + 1 == k:
            print(root.data, end=" ")
        else:
            printKDistanceNodeDown(root.left, k-dr-2)
        
        return 1 + dr
    
    return -1

# Driver program to test above function 
root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 
target = root.left 
printKDistanceNodes(root, target, 2)
print()
