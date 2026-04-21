from collections import deque


# ----------------------
# BST
# ----------------------

class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:

    def insert(self, root, key):

        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)

        else:
            root.right = self.insert(root.right, key)

        return root


    def search(self, root, key):

        if root is None:
            return False

        if root.key == key:
            return True

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)


    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)


    def min_value(self, node):

        while node.left:
            node = node.left

        return node


    def delete(self, root, key):

        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:

            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.min_value(root.right)

            root.key = temp.key

            root.right = self.delete(root.right, temp.key)

        return root


# ----------------------
# GRAPH
# ----------------------

class Graph:

    def __init__(self):

        self.graph = {}

    def add_edge(self, u, v, w):

        if u not in self.graph:
            self.graph[u] = []

        self.graph[u].append((v, w))


    def bfs(self, start):

        visited = set()

        queue = deque([start])

        while queue:

            node = queue.popleft()

            if node not in visited:

                print(node, end=" ")

                visited.add(node)

                for neighbor, _ in self.graph.get(node, []):
                    queue.append(neighbor)


    def dfs(self, node, visited=None):

        if visited is None:
            visited = set()

        visited.add(node)

        print(node, end=" ")

        for neighbor, _ in self.graph.get(node, []):

            if neighbor not in visited:
                self.dfs(neighbor, visited)


# ----------------------
# HASH TABLE
# ----------------------

class HashTable:

    def __init__(self, size):

        self.size = size

        self.table = [[] for _ in range(size)]


    def hash(self, key):

        return key % self.size


    def insert(self, key, value):

        index = self.hash(key)

        self.table[index].append((key, value))


    def get(self, key):

        index = self.hash(key)

        for k, v in self.table[index]:

            if k == key:
                return v

        return None


    def delete(self, key):

        index = self.hash(key)

        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):

            if k == key:
                bucket.pop(i)
                return


# ----------------------
# MAIN PROGRAM
# ----------------------

if __name__ == "__main__":

    print("BST TEST")

    bst = BST()

    root = None

    nums = [50,30,70,20,40,60,80]

    for n in nums:
        root = bst.insert(root, n)

    print("Inorder:")
    bst.inorder(root)

    print("\nSearch 20:", bst.search(root,20))
    print("Search 90:", bst.search(root,90))

    root = bst.delete(root,20)
    print("\nAfter deleting 20")
    bst.inorder(root)


    print("\n\nGRAPH TEST")

    g = Graph()

    edges = [
        ("A","B",2),("A","C",4),("B","D",7),
        ("B","E",3),("C","E",1),("D","F",5),
        ("E","D",2),("E","F",6),("C","F",8)
    ]

    for u,v,w in edges:
        g.add_edge(u,v,w)

    print("BFS:")
    g.bfs("A")

    print("\nDFS:")
    g.dfs("A")


    print("\n\nHASH TABLE TEST")

    ht = HashTable(5)

    keys = [10,15,20,7,12]

    for k in keys:
        ht.insert(k, str(k))

    print("Get 15:", ht.get(15))

    ht.delete(15)

    print("After delete 15:", ht.get(15))