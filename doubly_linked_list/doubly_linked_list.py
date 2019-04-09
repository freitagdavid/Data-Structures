"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f'<value: {self.value}>'

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __repr__(self):
        return self.get_items()

    def __str__(self):
        return str(self.get_items())

    def get_items(self):
        current_node = self.head
        return_list = []
        while current_node.next:
            return_list.append(current_node.value)
            current_node = current_node.next
        return_list.append(current_node.value)
        return(return_list)

    def add_to_head(self, value):
        if not self.head:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1

    def remove_from_head(self):
        if self.head is self.tail:
            self.tail = None
        current_node = self.head
        self.head = current_node.next
        current_node.delete()
        self.length -= 1
        return current_node.value

    def add_to_tail(self, value):
        if not self.head:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    def remove_from_tail(self):
        if self.tail is self.head:
            self.head = None
        current_node = self.tail
        self.tail = current_node.prev
        current_node.delete()
        self.length -= 1
        return current_node.value

    def move_to_front(self, node):
        if node is not self.head:
            self.delete(node)
            self.add_to_head(node.value)

    def move_to_end(self, node):
        if node is not self.tail:
            self.delete(node)
            self.add_to_tail(node.value)

    def delete(self, node):
        current_node = self.head
        if node is self.head:
            self.remove_from_head()
        elif node is self.tail:
            self.remove_from_tail()
        else:
            while current_node is not node:
                current_node = current_node.next
                current_node.delete()
                self.length -= 1

    def get_max(self):
        current_node = self.head
        highest_node = self.head
        while True:
            if current_node.next:
                if current_node.value > highest_node.value:
                    highest_node = current_node
                current_node = current_node.next
            else:
                if current_node.value > highest_node.value:
                    highest_node = current_node
                break
        return highest_node.value


node = ListNode(1)
linked_list = DoublyLinkedList(node)
linked_list.add_to_tail(10)

print(linked_list)
