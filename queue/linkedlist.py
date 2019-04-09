class List_Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)


class Linked_List:
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
        return return_list

    def prepend(self, value):
        current_head = self.head
        self.head = List_Node(value, current_head)
        self.length += 1

    def del_head(self):
        if self.head:
            current_head = self.head
            if current_head.next:
                self.head = current_head.next
                current_head.next = None
            else:
                self.head = None
                self.tail = None
            self.length -= 1
            return current_head.value
        return None

    def append(self, value):
        if self.head:
            self.tail.next = List_Node(value)
            self.tail = self.tail.next
        else:
            self.head = List_Node(value)
            self.tail = self.head
        self.length += 1

    def del_tail(self):
        current_tail = self.tail
        current_node = self.head
        while current_node.next:
            if current_node.next == current_tail:
                self.tail = current_node
                self.tail.next = None
                break
            current_node = current_node.next
        self.length -= 1
        return current_tail.value
