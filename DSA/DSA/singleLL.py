class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

# creating a node
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# connecting the nodes
node1.next = node2
node2.next = node3
node3.next = node4

# printing the nodes
n1 = node1
while(n1 != None):
    print(n1.data,end = " -> ")
    n1 = n1.next
print("None")


# New linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLL:
    def __init__(self):
        self.head = None

    def insertAtTheEnd(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp   # linking the new node

    def printLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next


obj = SingleLL()
obj.insertAtTheEnd(10)
obj.insertAtTheEnd(20)
obj.insertAtTheEnd(30)
obj.insertAtTheEnd(40)
obj.printLL()


# Insert at the begeining
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLL:
    def __init__(self):
        self.head = None

    def insertAtTheEnd(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp   # linking the new node

    def insertAtBeg(self,value): # inserts the value at the begeing
        temp = Node(value) 
        temp.next = self.head # prints the value --> 5
        self.head = temp # prints the other values

    def printLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next


obj = SingleLL()
obj.insertAtTheEnd(10)
obj.insertAtTheEnd(20)
obj.insertAtTheEnd(30)
obj.insertAtTheEnd(40)
obj.insertAtBeg(5)
obj.printLL()


# intert at the middle
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLL:
    def __init__(self):
        self.head = None

    def insertAtTheEnd(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp   # linking the new node

    def insertAtMid(self,value,x):
        temp = Node(value)
        t1 = self.head
        while(t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def printLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next


obj = SingleLL()
obj.insertAtTheEnd(10)
obj.insertAtTheEnd(20)
obj.insertAtTheEnd(30)
obj.insertAtTheEnd(40)
obj.insertAtMid(40,20)
obj.printLL()



# New linked list for deleting the data
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLL:
    def __init__(self):
        self.head = None

    def insertAtTheEnd(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp   # linking the new node

    def insertAtMid(self,value,x):
        temp = Node(value)
        t1 = self.head
        while(t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def deleteLL(self,value): # delete the value 
        t1 = self.head
        previous = t1
        if (self.head == value):
            self.head = t1.next
        while (t1.next != None):
            if(t1.data == value):
                previous.next = t1.next
                break
            else:
                previous = t1
                t1 = t1.next
        if(t1.data == value):
            previous.next = None
     
    def printLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next


obj = SingleLL()
obj.insertAtTheEnd(10)
obj.insertAtTheEnd(20)
obj.insertAtTheEnd(30)
# obj.insertAtMid(40,20)
obj.deleteLL(10)
obj.printLL()