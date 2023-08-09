# STACK IMPLEMENTATION USING ARRAYS

class k():
    def __init__(self):
        self.stack = list()
        self.maxsize = 5
        self.top = -1

    def push(self, data):
        if self.top == self.maxsize - 1:
            print("stack is full")
        else:
            self.top = self.top + 1
            self.stack.append(data)

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            item = self.stack.pop()
            self.top = self.top - 1
            print("deleted item:", item)

    def display(self):
        print(self.stack)

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print(self.stack[self.top])


bk = k()
while (1):
    print("1.push")
    print("2.pop")
    print("3.display")
    print("4.peek")
    print("5.exit")
    choice = int(input("enter your choice"))
    if choice == 1:
        value = int(input("enter the data"))
        bk.push(value)
    elif choice == 2:
        bk.pop()
    elif choice == 3:
        bk.display()
    elif choice == 4:
        bk.peek()
    else:
        break
