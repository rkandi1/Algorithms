import random

class UnsortedArrayMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value


    def __init__(self):
        self.table = []

    def __len__(self):
        return len(self.table)

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        for item in self.table:
            if key == item.key:
                return item.value
        raise KeyError("Key Error: " + str(key))

    def __setitem__(self, key, value):
        for item in self.table:
            if key == item.key:
                item.value = value
                return
        self.table.append(UnsortedArrayMap.Item(key, value))

    def __delitem__(self, key):
        for j in range(len(self.table)):
            if key == self.table[j].key:
                self.table.pop(j)
                return
        raise KeyError("Key Error: " + str(key))

    def __iter__(self):
        for item in self.table:
            yield item.key

class ChainingHashTableMap:

    def __init__(self, N=64, p=6460101079):
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        self.p = p
        self.a = random.randrange(1, self.p - 1)
        self.b = random.randrange(0, self.p - 1)
        self._new_lst = []
        self.pointer = -1
        self.first_index = 0

    def hash_function(self, k):
        return ((self.a * hash(k) + self.b) % self.p) % self.N

    def __len__(self):
        return self.n

    def __getitem__(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        return curr_bucket[key]

    def __setitem__(self, key, value):
        j = self.hash_function(key)
        if self.table[j] is None:
            self.table[j] = UnsortedArrayMap()
        old_size = len(self.table[j])
        self.pointer += 1
        self.table[j][key] = (value, self.pointer)
        if self.pointer == 0:
            self._new_lst.append([key, None, None])
        else:
            self._new_lst.append([key, self.pointer-1, None])
            self._new_lst[self._new_lst[len(self._new_lst)-1][1]][2] = self.pointer
        new_size = len(self.table[j])
        if (new_size > old_size):
            self.n += 1

    def __delitem__(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))

        del_val = self._new_lst[curr_bucket[key][1]]
        if del_val[2] is None:
            self._new_lst[del_val[1]][2] = del_val[2]
        elif del_val[1] is None:
            self.first_index = del_val[2]
            self._new_lst[del_val[2]][1] = del_val[1]
        else:
            self._new_lst[del_val[1]][2], self._new_lst[del_val[2]][1] = del_val[2], del_val[1]
        self._new_lst[curr_bucket[key][1]] = None
        del curr_bucket[key]

        self.n -= 1
        if (curr_bucket.is_empty()):
            self.table[j] = None
        if (self.n < self.N // 4):
            self.rehaash(self.N // 2)

    def __iter__(self):
        curr_node = self._new_lst[self.first_index]
        while curr_node[2] is not None:
            yield curr_node[0]
            curr_node = self._new_lst[curr_node[2]]
        yield curr_node[0]


    def rehash(self, new_size):
        old = []
        for key in self:
            value = self[key]
            old.append((key, value))
        self.table = [None] * new_size
        self.n = 0
        self._new_lst = []
        self.pointer = 0
        self.N = new_size
        for (key, value) in old:
            self[key] = value




if __name__=="__main__":
    ch = ChainingHashTableMap()
    ch[1] = 1
    ch[3] = "uno"
    ch[2] = 2
    ch[5] = 3
    ch[4] = 4
    ch[6236] = 6236

    for val in ch:
        print(val)
