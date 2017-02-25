class Node:

    def __init__(self, x):
        self.data = x
        self.next = None
class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, x):
        node = Node(x)
        if self.first == None:
            self.first = node
        elif self.last == None:
            self.last = self.first
            node.next = self.last
            self.first = node
        else:
            node.next = self.first
            self.first = node
        return
    
    def printSelf(self):
        currentNode = self.first
        while currentNode:
            if getattr(currentNode.data, 'data', None) == None:
                print(currentNode.data, end="")
            else:
                print(currentNode.data.data, end="")
                
            if currentNode.next != None:
                print(" -> ", end="")
            currentNode = currentNode.next
        print()
        

class Stack(LinkedList):

    def push(self, x):
        self.insert(x)
        return

    def pop(self):
        if self.first == None:
            raise Exception 
        top = self.first
        self.first = top.next
        if top.next == self.last:
            self.last = None
        return top.data

    def peek(self):
        if self.first == None:
            raise Exception 
        return self.first.data

class Queue(LinkedList):

    def add(self, x):
        node = x
        node.next = None
        if self.first == None:
            self.first = node
        elif self.last == None:
            self.first.next = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

        return

    def remove(self):
        data = self.first
        self.first = self.first.next 
        if self.first == self.last:
            self.last = None
        return data 

    def peek(self):
        return self.first.data if self.first != None else None

    def peekLast(self):
        return self.last.data if self.last != None else getattr(self.first, 'data', None)
     
    def isEmpty(self):
        return self.first == None

class MyQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def add(self, x):
        if self.stack1.first == None and self.stack2.first != None:
            self.transferStacks(self.stack2, self.stack1)
        self.stack1.push(x)

    def remove(self):
        if self.stack1.first == None and self.stack2.first == None:
            raise Exception
        else:
            if self.stack1.first != None and self.stack2.first == None:
                self.transferStacks(self.stack1, self.stack2)
            return self.stack2.pop()

    def peek(self):
        if self.stack1.first == None and self.stack2.first == None:
            raise Exception
        else:
            if self.stack1.first != None and self.stack2.first == None:
                self.transferStacks(self.stack1, self.stack2)
            return self.stack2.peek()

    def transferStacks(self, stackA, stackB):
        while stackA.first != None:
            stackB.push(stackA.pop())

