""" Question 5 """
class Node:
    def __init__(self, data, nxt = None, prev = None):
        self.data = data
        self.nxt = nxt
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.length = 0
        self.tail = Node(None, None, self.head)
        self.head.nxt = self.tail

    def __len__(self):
        return self.length

    def is_empty(self):
        return len(self) == 0

    def insert_head(self, val):
        new_node = Node(val, self.head.nxt, self.head)
        prev_node = self.head.nxt
        self.head.nxt = new_node
        prev_node.prev = new_node
        self.length += 1
        return self

    def add_last(self, val):
        new_node = Node(val, self.tail, self.tail.prev)
        prev_node = self.tail.prev
        self.tail.prev = new_node
        prev_node.nxt = new_node
        self.length+=1

    def add_after(self, node, elem):
        prev = node
        succ = node.nxt
        new_node = Node(elem, prev, succ)
        prev.next = new_node
        succ.prev = new_node
        self.length += 1
        return new_node

    def add_before(self, node, elem):
        return self.add_after(node.prev, elem)

    def remove_tail(self):
        del_node = self.tail.prev
        prev_node = self.tail.prev.prev
        self.tail.prev = prev_node
        prev_node.nxt = self.tail
        return del_node.data

    def last_node(self):
        return self.tail.prev

    def first_node(self):
        return self.head.nxt

    def remove_head(self):
        del_node = self.head.nxt
        nxt_node = self.head.nxt.nxt
        self.head.nxt = nxt_node
        nxt_node.prev = self.head
        return del_node.data

    def __iter__(self):
        if self.is_empty():
            return
        cursor = self.first_node()
        while cursor is not self.tail:
            yield cursor.data
            cursor = cursor.nxt

    def __str__(self):
        return '[' + '<-->'.join([str(elem) for elem in self]) + ']'

    def __repr__(self):
        return str(self)


def merge_sublists(srt_lnk_lst1, srt_lnk_lst2, lst1_val=None, lst2_val=None):
    # Checks if either or both lists are empty.
    if srt_lnk_lst1.is_empty() and srt_lnk_lst2.is_empty():
        return DoublyLinkedList()
    elif srt_lnk_lst1.is_empty():
        return srt_lnk_lst2
    elif srt_lnk_lst2.is_empty():
        return srt_lnk_lst1

    # Instantiates variables srt_lnk_lst1 and srt_lnk_lst2.
    if lst1_val is None:
        lst1_val = srt_lnk_lst1.first_node()
    if lst2_val is None:
        lst2_val = srt_lnk_lst2.first_node()

    # Instantiates the last node.
    last_node_1 = srt_lnk_lst1.last_node()
    last_node_2 = srt_lnk_lst2.last_node()

    if (lst1_val is last_node_1) and (lst2_val is last_node_2):
        new_dll = DoublyLinkedList()
        if last_node_1.data > last_node_2.data:
            new_dll.insert_head(last_node_1.data)
        else:
            new_dll.insert_head(last_node_2.data)
        return new_dll


    if lst1_val.data <= lst2_val.data:
        if lst1_val is last_node_1:
            dll = merge_sublists(srt_lnk_lst1, srt_lnk_lst2, lst1_val, lst2_val.nxt)
            dll.insert_head(lst2_val.data)
            return dll.insert_head(last_node_1.data)
        return merge_sublists(srt_lnk_lst1, srt_lnk_lst2, lst1_val.nxt, lst2_val).insert_head(lst1_val.data)
    else:
        if lst2_val is last_node_2:
            dll = merge_sublists(srt_lnk_lst1, srt_lnk_lst2, lst1_val.nxt, lst2_val)
            dll.insert_head(lst1_val.data)
            return dll.insert_head(last_node_2.data)
        return merge_sublists(srt_lnk_lst1, srt_lnk_lst2, lst1_val, lst2_val.nxt).insert_head(lst2_val.data)


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    return merge_sublists(srt_lnk_lst1, srt_lnk_lst2, srt_lnk_lst1.first_node(), srt_lnk_lst2.first_node())


if __name__ == "__main__":
    dll_1 = DoublyLinkedList()
    dll_1.add_last(2)
    dll_1.add_last(3)
    dll_1.add_last(5)
    dll_1.add_last(10)
    dll_1.add_last(15)
    dll_1.add_last(18)
    dll_1.add_last(19)
    dll_1.add_last(21)


    dll_2 = DoublyLinkedList()
    dll_2.add_last(1)
    dll_2.add_last(3)
    dll_2.add_last(5)
    dll_2.add_last(6)
    dll_2.add_last(8)
    dll_2.add_last(8)
    dll_2.add_last(11)

    print(merge_linked_lists(dll_1, dll_2))
