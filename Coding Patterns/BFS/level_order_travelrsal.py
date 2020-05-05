
class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def levelOrderTraversal(root: Node):
    if root is None:
        return []
    
    result = []
    queue = []
    queue.append(root)
    while( len(queue) > 0 ):
        current_level = []
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.pop(0)
            current_level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(current_level)
    return result

def zigzagTraversal(root: Node):
    if root is None:
        return []

    result = []
    queue = []
    queue.append(root)
    level = 1
    while( len(queue) > 0 ):
        current_level = []
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.pop(0)
            current_level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        if level%2 == 0:
            current_level.reverse()
            result.append(current_level)
        else:
            result.append(current_level)
        level += 1
    return result


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
print(zigzagTraversal(root))
