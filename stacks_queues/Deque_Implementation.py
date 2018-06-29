""" Question 2 """
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

class ArrayDeque:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayDeque.INITIAL_CAPACITY
        self.front = 0
        self.count = 0

    def _resize(self, capacity, in_front=False):
        if in_front:
            old = self.data
            self.data = [None] * capacity
            for i in range((len(self.data)//2)-1, len(self.data)):
                self.data[i] = old[(self.front + i) % len(old)]
            self.front = (len(self.data)//2)-1
        else:
            old = self.data
            self.data = [None] * capacity
            for i in range(self.count):
                self.data[i] = old[(self.front + i) % len(old)]
            self.front = 0

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count <= 0

    def first(self):
        return self.data[self.front]

    def last(self):
        back = (self.front+self.count) % len(self.data)
        return self.data[back]

    def add_first(self, val):
        if self.count == len(self.data):
            self._resize(2 * len(self.data), in_front=True)
        self.front -=1
        self.data[self.front] = val
        self.count += 1

    def add_last(self, elem):
        if self.count == len(self.data):
            self._resize(2 * len(self.data))
        back_ind = (self.front + self.count) % len(self.data)
        self.data[back_ind] = elem
        self.count += 1

    def delete_first(self):
        if (self.is_empty()):
            raise EmptyStack("Queue is empty")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.count -= 1
        if self.count < len(self.data) // 4:
            self._resize(len(self.data) // 2, in_front=True)
        return value

    def delete_last(self):
        if self.is_empty():
            raise EmptyStack()
        back_ind = ((self.front+self.count) % len(self.data)) - 1
        value = self.data[back_ind]
        self.data[back_ind] = None
        self.count -= 1
        if self.count < len(self.data) // 4:
            self._resize(len(self.data) // 2)
        return value

class MidStack:
    def __init__(self):
        self.data_one = ArrayStack()
        self.data_two = ArrayDeque()
        if len(self.data_one)%2 ==1:
            self.center = len(self.data_one) // 2 + 1
        else:
            self.center = len(self.data_one) / 2

    def is_empty(self):
        return len(self.data_one) == 0

    def __len__(self):
        return len(self.data_one) + len(self.data_two)

    def push(self,val):
        if self.data_two.is_empty():
            self.data_two.add_last(val)
        else:
            if len(self) % 2 == 0:
                self.data_one.push(self.data_two.delete_first())
                self.data_two.add_last(val)
            elif len(self) % 2 == 1:
                self.data_two.add_last(val)

    def top(self):
        if len(self.data) <= 0:
            raise EmptyStack
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise EmptyStack()
        value = self.data_two.delete_last()
        if len(self) % 2 == 1:
            self.data_two.add_first(value)

        return value

    def mid_push(self, val):
        if len(self) % 2 == 0:
            self.data_one.push(val)
        else:
            self.data_two.add_first(val)


if __name__ == "__main__":
    ms = MidStack()
    ms.push(2)
    ms.push(4)
    ms.push(6)
    ms.push(8)
    ms.push(10)
    ms.mid_push(10)
    print(ms.pop())
    print(ms.pop())
    print(ms.pop())
    print(ms.pop())
    print(ms.pop())
    print(ms.pop())