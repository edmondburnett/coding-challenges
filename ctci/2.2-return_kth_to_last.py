#!/usr/bin/env python


class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = Node()

    def append(self, data: int):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(data)

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    def kth(self, head: Node, k: int) -> int:
        """ Recursive solution """
        if head is None:
            return 0
        index = self.kth(head.next, k) + 1
        if index == k:
            print(f"{k}th to the last node is {head.data}")
        return index


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(13)
    ll.append(7)
    ll.append(5)
    ll.append(16)
    ll.append(9)
    ll.append(12)
    ll.append(64)

    ll.display()
    ll.kth(ll.head, 3)
