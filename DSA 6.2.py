# queue using linklist
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linklist:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data, None)

        if self.front is None:
            self.front = new_node
            self.rear = new_node

        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            return

        temp = self.front
        print("deqeue:", self.front.data)
        self.front = self.front.next
        temp = None

        if self.front is None:
            self.rear = None

    def display(self):
        n = self.front

        while n:
            print(n.data)
            n = n.next

    def peek(self):
        if self.front is None:
            print("Queue is Empty")
            return
        else:
            print(self.front.data)


INode = Linklist()
while (1):
    print("1.enqueue")
    print("2.dequeue")
    print("3.Display")
    print("4.peek")
    print("5.Exit")
    choice = int(input("enter your choice"))
    if choice == 1:
        node = int(input("enter the data"))
        INode.enqueue(node)
    elif choice == 2:
        INode.dequeue()
    elif choice == 3:
        INode.display()
    elif choice == 4:
        INode.peek()

    else:
        break