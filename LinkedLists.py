#Linked Lists

class createNode():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def append(self,data):
        newNode = createNode(data)
        if(self.head == None):
            self.head = newNode
            return
        
        elif(self.head):
            lastNode = self.head
            while(lastNode.next):
                lastNode = lastNode.next
            lastNode.next = newNode
            
    def prepend(self,data):
        if(self.head == None):
            return("Empty Linked List")
        newNode = createNode(data)
        newNode.next = self.head
        self.head = newNode
        
    def insertafter(self,pos,data):
        if(self.head == None):
            return("Empty Linked List")
        else:
            newNode = createNode(data)
            searchNode = self.head
            while(searchNode.data!=pos and searchNode.next!= None):
                searchNode = searchNode.next
                
            if(searchNode.data==pos):
                if(searchNode.next==None):
                    newNode.next =None
                else:
                    newNode.next = searchNode.next
                searchNode.next = newNode
            elif(searchNode.next==None):
                return("Node {} does not exit".format(pos))
            
    def delete(self,data):
        if(self.head == None):
            return("Empty Linked List")
        else:
            tempNode = self.head
            delNode = tempNode.next
            
        if(tempNode.next == None):
            self.head = None
            del(tempNode)
            return
        elif(tempNode.data == data):
            self.head = tempNode.next
            del(tempNode)
            return
        else:
            while(delNode.data!=data):
                delNode = delNode.next
                tempNode=tempNode.next
            if(delNode.data==data):
                tempNode.next = delNode.next
                del(delNode)
                
    def deleteat(self,pos):        
        if(self.head == None):
            return("Empty Linked List")
        else:
            i=0
            tempNode=self.head
            delNode=tempNode.next
            
        if(pos==0):
            self.head = tempNode.next
            del(tempNode)
        else:
            for i in range(pos-1):
                delNode = delNode.next
                tempNode = tempNode.next
                i+=1
            tempNode.next = delNode.next
            del(delNode)      
            
    def viewList(self):
        if(self.head == None):
            return ("Empty Linked List")
        
        else:
            currNode = self.head
            while(currNode):
                print(currNode.data)
                currNode = currNode.next
    
    def len(self):
        if(self.head==None):
            print(0)
        else:
            tempNode = self.head
        i=1
        while(tempNode.next):
            i+=1
            tempNode = tempNode.next
        else:
            print(i)

    
    def reverse(self):
        if(self.head == None):
            return("Empty Linked List")
        else:
            tempNode = self.head
            prev = None
            self.head = None
            
            while(tempNode.next):
                x = tempNode.next
                tempNode.next = prev
                prev = tempNode
                tempNode = x
            if(tempNode.next == None):
                tempNode.next = prev
                prev = tempNode
                self.head = tempNode
            
    
