""" Question 5 """
class ArrayStack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def __len__(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0

    def __getitem__(self, item):
        return self.data[item]

class EmptyStack(Exception):
    pass

class ArrayQueue:
    INITIAL_VALUE = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_VALUE
        self.front = 0
        self.nextInsert = 0  # Duplicate information
        self.count = 0

    def enqueue(self, val):
        if self.count >= len(self.data):
            self._resize(2*len(self.data))
        back = (self.front + self.count) % len(self.data)
        self.data[back] = val
        self.count += 1

    def __len__(self):
        return self.count

    def dequeue(self):
        if self.count == 0:
            raise EmptyStack()
        result = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.count -= 1
        return result

    def _resize(self, capacity):
        old = self.data
        self.data = [None] * capacity
        for i in range(self.count):
            self.data[i] = old[(self.front + i) % len(old)]
        self.front = 0

    def __str__(self):
        result = ""
        for i in range(self.front, len(self.data)):
            if i != len(self.data)-1:
                result += str(self.data[i])+ ", "
            else:
                result += str(self.data[i])
        return "["+result+"]"

def permutations(lst):
    perm_sets = ArrayQueue()
    perm_nums = ArrayStack()

    perm_sets.enqueue([])

    # for i in range(len(perm_nums)-1, -1, -1):
    for num in lst:
        for i in range(len(perm_sets)):
            val = perm_sets.dequeue()
            for j in range(len(val)+1):
                perm_nums.push(val[:j] + [num] + val[j:])
        perm_sets.enqueue(perm_nums)
        perm_nums = ArrayStack()

    temp = perm_sets.dequeue()
    for j in range(len(temp)):
        print(temp.pop())




print(permutations([1,2,3]))


