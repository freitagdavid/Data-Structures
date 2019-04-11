class Heap:
    def __init__(self):
        self.storage = []
        self.steps = 0

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        return_value = self.storage[0]
        self._swap(0, len(self.storage) - 1)
        del self.storage[-1]
        self._sift_down(0)
        return return_value

    def get_max(self):
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
        if self.storage[parent] < self.storage[current_node]:
            if current_node > 0:
                self._swap(current_node, parent)
                self._bubble_up(parent)
        # current_node = index
        # parent = self._parent(current_node)
        # while self.storage[parent] < self.storage[current_node]:
        #     if current_node <= 0:
        #         break
        #     self._swap(current_node, parent)
        #     current_node = parent
        #     parent = self._parent(current_node)

    def _sift_down(self, index):
        current = index
        left = self._left(current)
        right = self._right(current)
        if (self.get_size() > left) and (self.get_size() > right):
            if self.storage[left] >= self.storage[current] and self.storage[left] >= self.storage[right]:
                self._swap(left, current)
                self._sift_down(left)
            if self.storage[right] >= self.storage[current] and self.storage[right] >= self.storage[left]:
                self._swap(right, current)
                self._sift_down(right)
