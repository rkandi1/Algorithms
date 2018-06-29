""" Question 3 """
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

#####################################################################################################################

class CompactString:
    def __init__(self, org_str):
        self._org_str = org_str
        self.dll = DoublyLinkedList()

        if len(org_str) <= 0:
            self.dll.add_last(("", 1))
            return

        count = 0
        curr_char = org_str[0]
        for i in range(len(org_str)):
            if org_str[i] != curr_char:
                self.dll.add_last((curr_char, count))
                count = 1
                curr_char = org_str[i]
            else:
                count+=1

            if i == len(org_str) - 1:
                self.dll.add_last((curr_char, count))

    def __add__(self, other):
        new_comp_str = CompactString(self._org_str)
        curr_node = other.dll.first_node()
        for num in range(len(other.dll)):
            new_comp_str.dll.add_last(curr_node.data)
            curr_node = curr_node.next
        return new_comp_str

    def __lt__(self, other):
        self_curr_node = self.dll.first_node()
        other_curr_node = other.dll.first_node()
        for num in range(len(self.dll)):
            if self_curr_node.data[0] < other_curr_node.data[0]:
                return True
            elif self_curr_node.data[0] == other_curr_node.data[0]:
                if self_curr_node.data[1] > other_curr_node.data[1]:
                    other_curr_node = other_curr_node.next
                    if self_curr_node.data[0] < other_curr_node.data[0]:
                        return False
                elif self_curr_node.data[1] == other_curr_node.data[1]:
                    if self_curr_node is not self.dll.last_node():
                        self_curr_node = self_curr_node.next
                    if other_curr_node is not other.dll.last_node():
                        other_curr_node = other_curr_node.next

        return True

    def __le__(self, other):
        self_curr_node = self.dll.first_node()
        other_curr_node = other.dll.first_node()
        for num in range(len(other.dll)):
            if self_curr_node.data[0] <= other_curr_node.data[0]:
                return True
            elif self_curr_node.data[0] == other_curr_node.data[0]:
                if self_curr_node.data[1] > other_curr_node.data[1]:
                    other_curr_node = other_curr_node.next
                    if other_curr_node.data[0] > self_curr_node.data[0]:
                        return True
                elif self_curr_node.data[1] == self_curr_node.data[1]:
                    self_curr_node = self_curr_node.next
                    other_curr_node = other_curr_node.next

        if self == other:
            return True

        return False

    def __gt__(self, other):
        self_curr_node = self.dll.first_node()
        other_curr_node = other.dll.first_node()
        for num in range(len(self.dll)):
            if self_curr_node.data[0] > other_curr_node.data[0]:
                return True
            elif self_curr_node.data[0] == other_curr_node.data[0]:
                if self_curr_node.data[1] < other_curr_node.data[1]:
                    other_curr_node = other_curr_node.next
                    if self_curr_node.data[0] > other_curr_node.data[0]:
                        return True
                elif self_curr_node.data[1] == other_curr_node.data[1]:
                    if self_curr_node is not self.dll.last_node():
                        self_curr_node = self_curr_node.next
                    if other_curr_node is not other.dll.last_node():
                        other_curr_node = other_curr_node.next

        return False

    def __ge__(self, other):
        self_curr_node = self.dll.first_node()
        other_curr_node = other.dll.first_node()
        for num in range(len(other.dll)):
            if self_curr_node.data[0] >= other_curr_node.data[0]:
                return True
            elif self_curr_node.data[0] == other_curr_node.data[0]:
                if self_curr_node.data[1] < other_curr_node.data[1]:
                    other_curr_node = other_curr_node.next
                    if other_curr_node.data[0] >= self_curr_node.data[0]:
                        return True
                elif self_curr_node.data[1] == self_curr_node.data[1]:
                    self_curr_node = self_curr_node.next
                    other_curr_node = other_curr_node.next

        if self == other:
            return True

        return False

    def __str__(self):
        return str(self.dll)

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    s1 = CompactString('')
    s2 = CompactString('')
    print(s1 > s2)

