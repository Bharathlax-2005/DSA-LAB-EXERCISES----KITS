class kanishka:
    def __init__(self):
        self.queue = list()
        self.maxsize = int(input("Enter the size of the queue : "))
        self.queue = [None] * self.maxsize
        self.front = self.rear = -1

    def enqueue(self, data):
        if self.rear == self.maxsize - 1:
            print("Queue is full")
        else:
            if self.front == -1:
                self.front += 1
            self.rear += 1
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print(f'Deleted item : {self.queue[self.front]}')
            self.queue[self.front] = None
            self.front += 1

    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            i = self.front
            while i <= self.rear:
                print(self.queue[i], end=' --> ')
                i += 1

    def peek(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print(self.queue[self.rear])


seffania = kanishka()

while 1:
    print("\n1 : Enqueue")
    print("2 : Dequeue")
    print("3 : Peek")
    print("4 : Display")
    print("5 : Exit")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        value = int(input("Enter the value to be inserted : "))
        seffania.enqueue(value)
    elif choice == 2:
        seffania.dequeue()
    elif choice == 3:
        seffania.peek()
    elif choice == 4:
        seffania.display()
    else:
        break