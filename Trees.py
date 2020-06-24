class createNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree():
    def __init__(self, root):
        self.root = createNode(root)
    
    def recDFSPreorder(self, root):
        if(root == self.root):
            print("Recursive Preorder DFS  Traversal is:")
        if self.root is None:
            return
        else:
            print(root.data, end = " ")
            if root.left:
                self.recDFSPreorder(root.left)
            if root.right:
                self.recDFSPreorder(root.right)
         
    def recDFSInorder(self, root):
        if(root == self.root):
            print("Recursive Inorder DFS Traversal is: ")
        if self.root is None:
            return
        else:
            if root.left:
                self.recDFSInorder(root.left)
            print(root.data, end = " ")
            if root.right:
                self.recDFSInorder(root.right)
        
    def recDFSPostorder(self, root):
        if(root == self.root):
            print("Recursive Postorder DFS traversal is:")
        if self.root is None:
            return
        else:
            if root.left:
                self.recDFSPostorder(root.left)
            if root.right:
                self.recDFSPostorder(root.right)
            print(root.data, end = " ")
            
    def iDFSPreorder(self,root):
        print("Iterative Preorder DFS Traversal is: ")
        if self.root is None:
            return
        else:
            stack = []
            temp = self.root
            while(temp):
                print(temp.data, end= " ")
                stack.append(temp)
                temp = temp.left            
            while(True):
                if(stack == []):
                    return
                else:
                    temp = stack.pop()
                    temp = temp.right
                    while(temp):
                        print(temp.data, end= ' ')
                        stack.append(temp)
                        temp = temp.left
                        
    def iDFSInorder(self,root):
        print("Iterative Inorder DFS Traversal is: ")
        if self.root is None:
            return
        else:
            stack = []
            temp = self.root
            while(temp):
                stack.append(temp)
                temp = temp.left            
            while(True):
                if(stack == []):
                    return
                else:
                    temp = stack.pop()
                    print(temp.data, end = ' ')
                    temp = temp.right
                    while(temp):
                        stack.append(temp)
                        temp = temp.left
                        
    
    def iDFSPostorder(self, root):
        print("Iterative Postorder DFS Traversal is: ")
        if self.root is None:
            return
        else:
            stack = []
            value = []
            temp = self.root
            stack.append(temp)
            while(stack):
                temp = stack.pop()
                if(temp.left):
                    stack.append(temp.left)
                if(temp.right):
                    stack.append(temp.right)
            for i in value:
                print(i.data, end= " ")
    
    def BFS(self, root):
        if self.root is None:
            return
        else:
            print("BFS traversal is: ")
            temp = self.root
            queue = []
            queue.append(temp)
            while(queue):
                temp = queue.pop()
                temp.left, temp.right = temp.right, temp.left

                print(temp.data, end = " ")
                if(temp.left):
                    queue.insert(0,temp.left)
                if(temp.right):
                    queue.insert(0,temp.right)
