# #Stack implementation without size limit

# 1. List/Array
# 2. Linked List

# 1. Push - removes element permanently from the memory
# 2. Pop - 
# 3. Peek -  
# 4. isEmpty
# 5. isFull
# 6. Delete
# 7. display
import sys
class Stack:
    def __init__(self):
        self.myStack = []

    def push(self, value):
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

obj = Stack()
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