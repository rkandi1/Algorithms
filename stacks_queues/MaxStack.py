""" Question 4 """
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

class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.max_index = 0
        self.curr_index = 0

    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)

    def push(self, item):
        if self.curr_index == 0:
            self.data.push((item, None))
            self.curr_index += 1
        elif item > self.data[self.max_index][0]:
            self.data.push((item, self.max_index))
            self.max_index = self.curr_index
            self.curr_index +=1
        else:
            self.curr_index+=1
            self.data.push((item, None))

    def pop(self):
        if self.data.isEmpty():
            raise EmptyStack()
        self.curr_index -= 1
        value = self.data[self.curr_index]
        if self.data[self.max_index][0] == value[0]:
            self.max_index = value[1]
        return self.data.pop()


    def max(self):
        if self.data.isEmpty():
            raise EmptyStack
        return self.data[self.max_index][0]

if __name__ == "__main__":
    ms = MaxStack()
    ms.push(5)
    ms.push(-4)
    ms.push(4)
    ms.push(8)
    ms.push(6)
    ms.push(10)
    ms.pop()
    ms.pop()
    ms.pop()

    print(ms.max())


