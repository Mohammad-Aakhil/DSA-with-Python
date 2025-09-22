from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class Binray_ST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node

        else:
            curr = self.root
            while curr.value != value:
                if value < curr.value:
                    if curr.left is None:
                        curr.left = new_node
                        break
                    curr = curr.left

                else:
                    if curr.right is None:
                        curr.right = new_node
                        break
                    curr = curr.right
        return self
    
    def BFT(self):
        if self.root is None:
            return "BST is empty"
        
        else:
            queue = deque([self.root])
            visited = []
            while queue:
                node = queue.popleft()
                visited.append(node.value)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
        return visited
    
    def inorder(self,node, res=None):
        if res is None:
            res = []
        if node:
            self.inorder(node.left, res)
            res.append(node.value)
            self.inorder(node.right, res)
        return res


    def preorder(self, node):
        if node:
            print(node.value, end =" ")
            self.preorder(node.left)
            self.preorder(node.right)


    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end = " ")

    def kth_smallest_node(self, k):
        list = self.inorder(b.root)
        if k < 0 or k > len(list):
            return "index out or range"  
        return f"The node value at position '{k}' in BST from sorted order is '{list[k-1]}'"



b = Binray_ST()
b.insert(50)
b.insert(30)
b.insert(70)
b.insert(10)
b.insert(20)
b.insert(40)
b.insert(80)
print(b.BFT())
print(b.inorder(b.root))

print(b.kth_smallest_node(5))

b.inorder(b.root)[3]

