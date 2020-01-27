class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.last = None

    def addToEmpty(self, data):
        if self.last != None:
            return self.last

        # creating the new node
        temp = Node(data)
        self.last = temp
        # Create the link
        self.last.next = self.last
        return self.last

    def addBegin(self, data):
        if self.last == None:
            return self.addToEmpty(data)

        # creating a new node
        temp = Node(data)
        # Create the link
        temp.next = self.last.next
        self.last.next = temp
        return self.last

    def addEnd(self, data):
        if self.last == None:
            return self.addToEmpty(data)

        # Creating a new node
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        self.last = temp
        return self.last

    def addAfter(self, data, item):
        if self.last == None:
            return None

        temp = Node(data)
        p = self.last.next
        while p:
            if p.data == item:
                temp.next = p.next
                p.next = temp

                if p == self.last:
                    self.last = temp
                    return self.last
                else:
                    return self.last
            p = p.next
            if p == self.last.next:
                print('Item not found')
                break

    def traverse(self):
        if self.last == None:
            print('List is empty')
            return

        temp = self.last.next
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
            if temp == self.last.next:
                break




# Driver Code 
if __name__ == '__main__': 
  
    llist = CircularLinkedList() 
  
    last = llist.addToEmpty(6) 
    last = llist.addBegin(4) 
    last = llist.addBegin(2) 
    last = llist.addEnd(8) 
    last = llist.addEnd(12) 
    last = llist.addAfter(10,8) 
  
    llist.traverse() 
