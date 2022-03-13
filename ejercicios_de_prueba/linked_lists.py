class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class List:
    def __init__(self, root):
        self.root = root

    def append(self, value):
        current = self.root
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def show(self):
        current = self.root
        print("[", end='')
        while current is not None:
            print(current.val, end=", ")
            current = current.next
        print("]")

    def size(self):
        total = 0
        current = self.root
        while current is not None:
            current = current.next
            total += 1
        return total

    def reverse(self):
        previous = None
        current = self.root
        while current is not None:
            future = current.next
            current.next = previous
            previous = current
            current = future
        self.root = previous

            # current.next, current, previous = previous, current.next, current

lista = List(Node(1))

for i in range(2, 9):
    lista.append(i)

lista.show()
print(lista.size())
lista.reverse()
lista.show()
print(lista.size())
