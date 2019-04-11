# class Heap:
#   def __init__(self, comparator):
#     self.storage = []
#     self.comparator = comparator

#   def insert(self, value):
#     pass

#   def delete(self):
#     pass

#   def get_priority(self):
#     pass

#   def get_size(self):
#     pass

#   def _bubble_up(self, index):
#     pass

#   def _sift_down(self, index):
#     pass


class Heap:
    def __init__(self, comparator=lambda x, y: x > y):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        return_value = self.storage[0]
        self._swap(0, len(self.storage) - 1)
        del self.storage[-1]
        self._sift_down(0)
        return return_value

    def get_priority(self):
        return self.storage[0]

    def _swap(self, index_a, index_b):
        temp = self.storage[index_a]
        self.storage[index_a] = self.storage[index_b]
        self.storage[index_b] = temp

    def get_size(self):
        return len(self.storage)

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return (index * 2) + 1

    def _right(self, index):
        return (index * 2) + 2

    def _bubble_up(self, index):
        current_node = index
        parent = self._parent(current_node)
        if self.comparator(self.storage[current_node], self.storage[parent]):
            if current_node > 0:
                self._swap(current_node, parent)
                self._bubble_up(parent)

    def _sift_down(self, index):
        current = index
        left = self._left(current)
        right = self._right(current)
        size = self.get_size()
        left_exist = size > left
        right_exist = size > right
        if left_exist and right_exist:
            if (self.comparator(self.storage[left], self.storage[current]) and self.comparator(self.storage[left], self.storage[right])) or (self.storage[left] == self.storage[right]):
                self._swap(left, current)
                self._sift_down(left)
            if (self.comparator(self.storage[right], self.storage[current]) and self.comparator(self.storage[right], self.storage[left])) or (self.storage[right] == self.storage[left]):
                self._swap(right, current)
                self._sift_down(right)
        if left_exist:
            if self.comparator(self.storage[left], self.storage[current]):
                self._swap(left, current)
        if right_exist:
            if self.comparator(self.storage[right], self.storage[current]):
                self._swap(right, current)
