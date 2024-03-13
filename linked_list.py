from collections.abc import Iterable
from typing import Iterator


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)


class LinkedList(Iterable):
    def __init__(self):
        self.Head = None

    def __iter__(self) -> Iterator:
        return super().__iter__()

    def printList(self):
        current = self.Head
        while current is not None:
            print(current.data, end=" " + "\n")
            current = current.next

    def getLength(self):
        count = 0
        current = self.Head
        while current is not None:
            count += 1
            current = current.next
        return count

    def append_first(self, number):
        n = self.Head
        self.Head = Node(number)
        self.Head.next = n

    def append_last(self, number):
        new_node = Node(number)
        if self.Head is None:
            self.Head = new_node
        else:
            curr = self.Head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def append_at_position(self, number, position):
        counter = 1
        current = self.Head
        while counter < position - 1 and current is not None:
            counter += 1
            current = current.next
        if position == 1:
            new_node = Node(number)
            new_node.next = current
            self.Head = new_node
        else:
            new_node = Node(number)
            new_node.next = current.next
            current.next = new_node

    def delete_first(self):
        if self.Head is None:
            return
        else:
            node = self.Head
            self.Head = self.Head.next
            del node

    def delete_last(self):
        if self.Head is None:
            return
        else:
            current = self.Head
            previous = None
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None
            del current

    def deleteAtPosition(self, position):
        if self.Head is None:
            return
        else:
            current = self.Head
            previous = None
            count = 1
            while current.next is not None and count < position:
                previous = current
                current = current.next
                count += 1
            if current == self.Head:
                self.Head = current.next
                del current
            else:
                previous.next = current.next
                del current


if __name__ == '__main__':
    list = LinkedList()
    list.append_last(1)
    list.append_last(2)
    list.append_first(3)
    list.append_at_position(8, 1)
    list.deleteAtPosition(2)
    list.printList()
    print("länge:", list.getLength())
