from linkedlist import Linked_List


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = Linked_List()

    def enqueue(self, item):
        self.storage.append(item)

    def dequeue(self):
        return self.storage.del_head()

    def len(self):
        return len(self.storage)
