""" Question 1 """

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

class Queue:
    def __init__(self):
        self.data_one = ArrayStack()
        self.data_two = ArrayStack()
        self.first_index = 0
        self.count = 0

    def __len__(self):
        return self.count

    def enqueue(self, value):
        self.data_one.push(value)
        self.count+=1

    def dequeue(self):
        if self.data_one.isEmpty():
            raise EmptyStack()
        if self.data_two.isEmpty():
            for index in range(len(self.data_one)-1, self.first_index, -1):
                self.data_two.push(self.data_one[index])
        self.first_index += 1
        self.count -= 1
        return self.data_two.pop()

    def is_empty(self):
        return self.count <= 0

    def first(self):
        return self.data_one[self.first_index]

    def __str__(self):
        result = ""
        for i in range(self.first_index, len(self.data_one)):
            if i != len(self.data_one)-1:
                result += str(self.data_one[i])+ ", "
            else:
                result += str(self.data_one[i])
        return "["+result+"]"

if __name__ == "__main__":
    Q = Queue()
    Q.enqueue(3)
    Q.enqueue(4)
    Q.dequeue()
    print(str(Q))

