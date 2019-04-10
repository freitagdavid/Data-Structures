class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        return_value = self.storage[0]
        self._swap(0, len(self.storage) - 1)
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
        parent_index = (index - 1) // 2
        return self._return_node(parent_index)

    def _left(self, index):
        left_index = (index * 2) + 1
        return self._return_node(left_index)

    def _right(self, index):
        right_index = (index * 2) + 2
        return self._return_node(right_index)

    def _return_node(self, index):
        if index <= self.get_size() and not index < 0:
            return {'index': index, 'value': self.storage[index]}
        return None

    def _bubble_up(self, index):
        current_node = self._return_node(index)
        parent = self._parent(index)
        while parent['value'] < current_node['value']:
            if current_node['index'] <= 0:
                break
            self._swap(current_node['index'], parent['index'])
            current_node = self._parent(current_node['index'])
            parent = self._parent(current_node['index'])

    def _sift_down(self, index):
        current_index = index
        current_node = self._return_node(current_index)
        right_child = self._right(current_node['index'])
        while current_node['value'] < right_child['value']:
            if not right_child:
                break
            elif right_child['value'] > current_node['value']:
                self._swap(right_child['index'], current_node['index'])
                current_index = right_child['index']
                current_node = self._return_node(current_index)
                right_child = self._right(current_node['index'])
            else:
                break
