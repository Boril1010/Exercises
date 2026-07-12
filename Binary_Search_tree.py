class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    def insert(self,root, new_key):
        if root == None:
            return Node(new_key)
        elif root.val == new_key:
            return root
        if root.val < new_key:
            root.right = self.insert(root.right, new_key)
        else:
            root.left = self.insert(root.left, new_key)
        return root

    def traverse(self,root):
        if root:
            self.traverse(root.left)
            print(root.val)
            self.traverse(root.right)

    def search(self,root,key):

        if root == None or root.val == key:
            return root

        if root.val < key:
            return self.search(root.right,key)

        return self.search(root.left,key)




root = Node(25)
root.insert(root, 10)
root.insert(root, 30)
root.insert(root, 20)

root.traverse(root)

print(root.search(root,8)) # -- None
