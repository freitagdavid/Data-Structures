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
        current_exist = size > current
        left_exist = size > left
        right_exist = size > right
        current_value = self.storage[current] if current_exist else None
        left_value = self.storage[left] if left_exist else None
        right_value = self.storage[right] if right_exist else None
        if left_exist and right_exist:
            if (self.comparator(left_value, current_value) and self.comparator(left_value, right_value)) or (left_value == right_value):
                self._swap(left, current)
                self._sift_down(left)
            if (self.comparator(left_value, current_value) and self.comparator(right_value, left_value)) or (right_value == left_value):
                self._swap(right, current)
                self._sift_down(right)
        if left_exist:
            # For some reason current_value isn't working here.
            if self.comparator(left_value, self.storage[current]):
                self._swap(left, current)
        if right_exist:
            if self.comparator(right_value, self.storage[current]):
                self._swap(right, current)
