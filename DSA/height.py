class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return 0

    else:

        lDepth = height(node.left)
        rDepth = height(node.right)

        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)

print(height(root))
