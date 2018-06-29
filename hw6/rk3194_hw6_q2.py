""" Question 2 """
class Empty(Exception):
    pass


class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if (self.is_empty()):
            raise Empty("List is empty")
        return self.header.next

    def last_node(self):
        if (self.is_empty()):
            raise Empty("List is empty")
        return self.trailer.prev

    def add_first(self, elem):
        return self.add_after(self.header, elem)

    def add_last(self, elem):
        return self.add_after(self.trailer.prev, elem)

    def add_after(self, node, elem):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node()
        new_node.data = elem
        new_node.prev = prev
        new_node.next = succ
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_before(self, node, elem):
        return self.add_after(node.prev, elem)

    def delete(self, node):
        prev = node.prev
        succ = node.next
        prev.next = succ
        succ.prev = prev
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def __iter__(self):
        if(self.is_empty()):
            return
        cursor = self.first_node()
        while(cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return '[' + '<-->'.join([str(elem) for elem in self]) + ']'

    def __repr__(self):
        return str(self)

##################################################################################################################

class Integer:
    def __init__(self, num_str):
        self.dll = DoublyLinkedList()
        for num in num_str:
            self.dll.add_last(num)

    def __add__(self, other):
        zero_val = ord("0")
        new_dll = DoublyLinkedList()

        if len(self.dll) > len(other.dll):
            i = len(self.dll) - len(other.dll)
            while i != 0:
                other.dll.insert_head("0")
                i-=1
        elif len(self.dll) < len(other.dll):
            i = len(other.dll) - len(self.dll)
            while i != 0:
                self.dll.add_first("0")
                i -= 1

        curr_node_self = self.dll.first_node()
        curr_node_other = other.dll.first_node()
        prev_num = 0

        for num in range(len(self.dll)):
            self_diff = ord(curr_node_self.data) - zero_val
            other_diff = ord(curr_node_other.data) - zero_val
            result = self_diff + other_diff
            if result >= 10:
                if curr_node_self == self.dll.first_node():
                    temp = result
                    result = str(result)
                    new_dll.add_last(result[0])
                    new_dll.add_last(result[1])
                    curr_node_other = curr_node_other.next
                    curr_node_self = curr_node_self.next
                    prev_num = temp % 10
                else:
                    new_dll.last_node().data = str(prev_num + result//10)
                    new_dll.add_last(str(result % 10))
                    curr_node_other = curr_node_other.next
                    curr_node_self = curr_node_self.next
                    prev_num = result % 10

            else:
                new_dll.add_last(str(result))
                prev_num = result
                curr_node_other = curr_node_other.next
                curr_node_self = curr_node_self.next


        return new_dll

    def __str__(self):
        return str(self.dll)

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    I1 = Integer("1")
    I2 = Integer("2048")
    I3 = I1 + I2
    print(I3)
