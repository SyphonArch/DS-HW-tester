"""PriorityQueue class implemented by SyphonArch.

Methods constructed to mirror std::priority_queue of C++.

std::priority_queue::emplace and std::priority_queue::swap has been left out
as I really don't see the need for them in Python(plus I'm lazy lol)."""


class PriorityQueue:
    def __init__(self, key=lambda x: x):
        self._max_heap = []
        self._compare = lambda x, y: key(x) <= key(y)

    # Private methods
    @staticmethod
    def _left_child(i):
        return i * 2 + 1

    @staticmethod
    def _right_child(i):
        return i * 2 + 2

    @staticmethod
    def _parent(i):
        return (i - 1) // 2

    def _largest(self, i, j, k):
        in_range = [idx for idx in (i, j, k) if 0 <= idx < self.size()]
        pairs = [(idx, self._max_heap[idx]) for idx in in_range]
        tmp_largest = pairs[0]
        for idx, val in pairs[1:]:
            if self._compare(tmp_largest[1], val):
                tmp_largest = (idx, val)
        return tmp_largest[0]

    def _swap(self, i, j):
        self._max_heap[i], self._max_heap[j] = self._max_heap[j], self._max_heap[i]

    def _percolate_up(self, i):
        curr = i
        while curr != 0:
            parent = PriorityQueue._parent(curr)
            left = PriorityQueue._left_child(parent)
            right = PriorityQueue._right_child(parent)
            largest = self._largest(parent, left, right)
            self._swap(parent, largest)
            curr = parent

    def _percolate_down(self, i):
        curr = i
        while curr < self.size():
            parent = curr
            left = PriorityQueue._left_child(curr)
            right = PriorityQueue._right_child(curr)
            largest = self._largest(parent, left, right)
            if largest != curr:
                self._swap(parent, largest)
                curr = largest
            else:
                break

    def __repr__(self):
        lines = []
        level = 0
        location = 0
        while location < self.size():
            level_size = pow(2, level)
            lines.append(" ".join(map(str, self._max_heap[location: location + level_size])))
            location += level_size
            level += 1
        return "[" + "\n".join(lines) + "]"

    # Element access
    def top(self):
        return self._max_heap[0]

    # Capacity
    def empty(self):
        return len(self._max_heap) == 0

    def size(self):
        return len(self._max_heap)

    # Modifiers
    def push(self, value):
        self._max_heap.append(value)
        self._percolate_up(len(self._max_heap) - 1)

    def pop(self):
        self._swap(0, self.size() - 1)
        popped_value = self._max_heap.pop()
        self._percolate_down(0)
        return popped_value

    # Extra features
    def __bool__(self):
        return not self.empty()
