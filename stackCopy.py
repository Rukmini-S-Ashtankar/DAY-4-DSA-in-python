# Now you have to implement with size limit
import sys
class Stack:
    def __init__(self, size):
        self.myStack = []             #creating Stack
        self.sizeStack = size   # stack size defined
    
    def isFull(self):
        if len(self.myStack) == self.sizeStack:        #If the existing stack size is equal to the stack size defined in the sizeStack then true or else false means element can be entered
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():                          #isFull() is called here so that if extra element is pushed, it will print stack is full
            print("Stack is Full")                      
        else:                                      #if not full then element can be pushed in the stack
            self.myStack.append(value)
            print("Element Push")

    def display(self):
        print(self.myStack)
    
    def isEmpty(self):
        if self.myStack == []:              #if stack is empty then True
            return True                       
        else:                               #or it will go in else and return False
            return False
        
    def pop(self):
        if self.isEmpty():
             print("Stack is empty")         #pop 1st checks if the stack is empty
        else:
            print(self.myStack.pop())

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.myStack[-1])

    def deleteStack(self):
        self.myStack = None           #if None is assigne then it's memory is erased

size = int(input("Enter the size of Stack: "))

obj = Stack(size)              #value passed to the constructor
print("Stack has created: ")
while True:
    print("Stack has created: ")
    print("1. Push Ooperation: ")
    print("2. Display Stack")
    print("3. Pop Operation: ")
    print("4. Peek Operation: ")
    print("5. Delete Stack")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter value to push in stack:"))
        obj.push(value)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.pop()                     #removes elements one by one #Ex: 3,5,7 will be poped like 7 then 5 then 3
    elif choice == 4:
        obj.peek()
    elif choice == 5:
        obj.deleteStack()                    # only returns top element and is not removed from stack. # ex: 2,4,8 returns 8
    else:
        sys.exit()