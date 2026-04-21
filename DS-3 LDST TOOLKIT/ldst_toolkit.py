# -------------------------------
# Dynamic Array Implementation
# -------------------------------

class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = x
        self.size += 1
        print(f"Inserted {x} | Size: {self.size} | Capacity: {self.capacity}")

    def resize(self):
        print("Resizing array...")
        self.capacity *= 2
        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def pop(self):
        if self.size == 0:
            print("Array empty")
            return None

        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return val

    def display(self):
        print("Array:", self.arr[:self.size])


# -------------------------------
# Node for Linked Lists
# -------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# -------------------------------
# Singly Linked List
# -------------------------------

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def insert_at_end(self, x):
        new = Node(x)

        if not self.head:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new

    def delete_by_value(self, x):

        if not self.head:
            return

        if self.head.data == x:
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next

        while curr:
            if curr.data == x:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# -------------------------------
# Doubly Linked List
# -------------------------------

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert_after(self, target, x):
        temp = self.head

        while temp:
            if temp.data == target:
                new = Node(x)

                new.next = temp.next
                new.prev = temp

                if temp.next:
                    temp.next.prev = new

                temp.next = new
                return

            temp = temp.next

    def delete_at_position(self, pos):

        if not self.head:
            return

        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for i in range(pos):
            temp = temp.next
            if temp is None:
                return

        if temp.prev:
            temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev


# -------------------------------
# Stack using Linked List
# -------------------------------

class Stack:

    def __init__(self):
        self.head = None

    def push(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def pop(self):
        if not self.head:
            print("Stack Underflow")
            return None

        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        if not self.head:
            return None
        return self.head.data


# -------------------------------
# Queue using Linked List
# -------------------------------

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new = Node(x)

        if not self.head:
            self.head = self.tail = new
            return

        self.tail.next = new
        self.tail = new

    def dequeue(self):

        if not self.head:
            print("Queue Underflow")
            return None

        val = self.head.data
        self.head = self.head.next

        if not self.head:
            self.tail = None

        return val

    def front(self):
        if not self.head:
            return None
        return self.head.data


# -------------------------------
# Balanced Parentheses Checker
# -------------------------------

def is_balanced(expr):

    stack = Stack()

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in expr:

        if ch in "({[":
            stack.push(ch)

        elif ch in ")}]":
            if stack.peek() == pairs[ch]:
                stack.pop()
            else:
                return False

    return stack.peek() is None


# -------------------------------
# MAIN PROGRAM
# -------------------------------

if __name__ == "__main__":

    print("---- Dynamic Array Test ----")
    arr = DynamicArray(2)

    for i in range(10):
        arr.append(i)

    arr.display()

    print("Pop:", arr.pop())
    print("Pop:", arr.pop())
    print("Pop:", arr.pop())

    arr.display()


    print("\n---- Singly Linked List Test ----")

    sll = SinglyLinkedList()

    sll.insert_at_beginning(10)
    sll.insert_at_beginning(5)
    sll.insert_at_beginning(1)

    sll.insert_at_end(20)
    sll.insert_at_end(30)
    sll.insert_at_end(40)

    sll.traverse()

    sll.delete_by_value(20)

    print("After deleting 20:")
    sll.traverse()


    print("\n---- Stack Test ----")

    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("Peek:", stack.peek())


    print("\n---- Queue Test ----")

    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Front:", queue.front())
    print("Dequeue:", queue.dequeue())
    print("Front:", queue.front())


    print("\n---- Parentheses Checker ----")

    tests = ["([])", "([)]", "(((", ""]

    for t in tests:
        print(t, "->", "Balanced" if is_balanced(t) else "Not Balanced")