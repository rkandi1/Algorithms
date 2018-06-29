""" Question 2 """
"""
Created June 19, 2017
min_heap.py

Heap in which it is assumed that the keys are the same as the values,
so entries only consist of a single item, not a (key,value) pair.

Only handling a min_heap here. Could swap the comparisons to make it a max_heap
or use the operator functions as done in heap.py
"""

class Heap:
    def __init__(self, seq=None):
        self._data = seq if seq else []
        self._size = len(self._data)
        if len(self._data): self.heapify()

    def __len__(self):
        """Return the size of the heap"""
        return self._size

    def is_empty(self):
        """Return True is the heap is empty and False otherwise"""
        return self._size == 0

    def min(self):
        """Return the 'smallest' value"""
        if self._size == 0: raise KeyError  # Nothing to return if heap empty
        return self._data[0]           # so simple!

    def add(self, value):
        """add value to the heap"""
        # Does the underlying "array" have enough space? If not
        # increase its size.  Note, we are really using a Python list
        # as our underlying data structure, so any "doubling" is
        # handled for us.
        if len(self) == len(self._data): self._data.append(None)
        self._data[self._size] = value   # insert new item at end of arry
        self.up_heap(self._size)         # "bubble" the new item up.
        self._size += 1                  # bump the sze

    def remove_min(self):
        """Remove the smallest value"""
        # Should raise an exception of size is 0...
        if self._size == 0: raise KeyError  # Can't remove from an empty heap
        result = self._data[0]         # remember the smallest
        self._data[0] = None           # None is so we don't have a reference.
        self._size -= 1                # don't forget we have one less
        # bring the last to the front and stick the None at the end
        self.swap(0, self._size)
        # and let the item inserted at the front "drift down"
        self.down_heap(0)
        return result                  # finally return what was the minimum

    def up_heap(self, index):
        """Bubble up the item at index, as needed"""
        while index:                       # while not at the root
            parent = self._parent(index)   # who is my parent?
            # Am I smaller than my parent?
            if self._data[index][1] < self._data[parent][1]:
                self.swap(index, parent)         # if so, swap me and my parent
                index = parent                   # and continue bubbling up
            else:
                return                           # otherwise we are done

    def down_heap(self, index):
        """
        down_heap: 'Sift' the item at index down, as needed
        """
        while not self._is_leaf(index):  # While we have room to sift down to
            min_child = index * 2 + 1    # Assuming left is the smaller child
            if self._has_right(index):   # If I have a right child, then check
                # is it is smaller
                if self._data[self._right(index)] < self._data[min_child]:
                    min_child = self._right(index)         # right is smaller
            if self._data[min_child] < self._data[index]:  # Is child smaller?
                self.swap(index, min_child) # Yes, swapping with smaller child
                index = min_child           # And continuing to sift down
            else:
                return                      # children were both larger

    def heapify(self):
        """
        Convert data into a heap
        """
        if self._size:
            start = self._parent(len(self._data)-1)  # who'se the last parent?
            for index in range(start, -1, -1):       # for all parents
                self.down_heap(index)                #   fix your heap

    # Possibly convenient functions
    def swap(self, i, j):
        """Swap items at indices i and j"""
        self._data[i], self._data[j] = self._data[j], self._data[i]


    def _is_leaf(self, index):
        """Is index a leaf? Check if it has a left child"""
        return 2*index+1 > self._size - 1

    def _parent(self, index):
        """Where is index's parent?"""
        # Declaring the "root" its own parent, otherwise usual math
        return (index - 1) // 2 if index else 0

    def _has_left(self, index):
        """Does index have a left child?"""
        return self._left(index) < len(self)

    def _left(self, index):
        """Where will index's left child be, if it exists?"""
        return 2*index + 1

    def _has_right(self, index):
        """Does index have a right child?"""
        return self._right(index) < len(self)

    def _right(self, index):
        """Where will index's right child be, if it exists?"""
        return 2*index + 2

    def __str__(self):
        result = []
        i=0
        while i != len(self._data):
            if self._data[i] is None:
                break
            result.append(self._data[i][0])
            i+=1
        return str(result)


class Queue:
    def __init__(self):
        self.p_queue = Heap()
        self.pointer = 0

    def __len__(self):
        return len(self.p_queue)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, value):
        self.p_queue.add((value, self.pointer))
        self.pointer+=1

    def dequeue(self):
        if self.is_empty(): raise KeyError
        return self.p_queue.remove_min()

    def __str__(self):
        return str(self.p_queue)


