# aert_toolkit.py
# PART A: Stack ADT

class StackADT:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)



# PART B: Factorial (Recursive)

def factorial(n):
    if n < 0:
        return "Invalid Input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Fibonacci

naive_calls = 0
memo_calls = 0

def fib_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


def fib_memo(n, memo=None):
    global memo_calls
    memo_calls += 1

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
        return n

    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


# PART C: Tower of Hanoi

def hanoi(n, source, auxiliary, destination, stack=None):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        if stack:
            stack.push(move)
        return

    hanoi(n-1, source, destination, auxiliary, stack)

    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    if stack:
        stack.push(move)

    hanoi(n-1, auxiliary, source, destination, stack)



# PART D: Recursive Binary Search

def binary_search(arr, key, low, high, stack=None):
    if low > high:
        return -1

    mid = (low + high) // 2

    if stack:
        stack.push(mid)

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1, stack)
    else:
        return binary_search(arr, key, mid + 1, high, stack)



# MAIN FUNCTION

def main():
    print("AERT Toolkit Outputs\n")

    # Factorial Test Cases

    print("---- Factorial Test Cases ----")
    for n in [0, 1, 5, 10]:
        print(f"factorial({n}) = {factorial(n)}")


    # Fibonacci Test Cases

    print("\n---- Fibonacci Test Cases ----")
    for n in [5, 10, 20, 30]:
        global naive_calls, memo_calls
        naive_calls = 0
        memo_calls = 0

        naive_result = fib_naive(n)
        memo_result = fib_memo(n)

        print(f"\nFibonacci({n})")
        print(f"Naive Result: {naive_result}, Calls: {naive_calls}")
        print(f"Memo Result: {memo_result}, Calls: {memo_calls}")

    # Tower of Hanoi 

    print("\n---- Tower of Hanoi (N=3) ----")
    stack = StackADT()
    hanoi(3, 'A', 'B', 'C', stack)

    print("\nStored Moves in Stack:")
    while not stack.is_empty():
        print(stack.pop())

  
    # Binary Search Test Cases

    print("\n---- Binary Search Test Cases ----")

    arr1 = [1,3,5,7,9,11,13]
    tests = [7,1,13,2]

    for key in tests:
        stack = StackADT()
        result = binary_search(arr1, key, 0, len(arr1)-1, stack)
        print(f"\nSearch {key} -> Index: {result}")
        print("Mid indices visited:", stack.items)

    # Empty list test

    arr2 = []
    result = binary_search(arr2, 5, 0, len(arr2)-1)
    print(f"\nSearch in empty list -> Index: {result}")


if __name__ == "__main__":
    main()