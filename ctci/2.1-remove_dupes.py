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

    def delete_dupes(self):
        encountered = []
        n = self.head
        previous = Node(None)
        while n is not None:
            if n.data in encountered:
                previous.next = n.next
            else:
                encountered.append(n.data)
                previous = n
            n = n.next

    def delete_dupes_nobuffer(self):
        """ Delete dupes without using a container/buffer """
        current = self.head
        while current is not None:
            runner = current
            while runner.next is not None:
                if (runner.next.data == current.data):
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(13)
    ll.append(7)
    ll.append(7)
    ll.append(5)
    ll.append(5)
    ll.append(16)
    ll.append(16)
    ll.append(13)

    ll.display()
    ll.delete_dupes_nobuffer()
    ll.display()
