""" Question 2 """
class BinarySearchTreeMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value


    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None
            self.index = 0
            self.rank = None

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None
            self.rank = None


    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    # raises exception if not found
    def __getitem__(self, key):
        node = self.subtree_find(self.root, key)
        if (node is None):
            raise KeyError(str(key) + " not found")
        else:
            return node.item.value

    # returns None if not found
    def subtree_find(self, subtree_root, key, delete=False):
        curr = subtree_root
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                curr = curr.left
            else:  # (curr.item.key < key)
                curr = curr.right
        return None


    # updates value if key already exists
    def __setitem__(self, key, value):
        node = self.subtree_find(self.root, key)
        if (node is None):
            self.subtree_insert(key, value)
        else:
            node.item.value = value

    # assumes key not in tree
    def subtree_insert(self, key, value=None):
        item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(item)
        if (self.is_empty()):
            self.root = new_node
            self.root.rank = 1
            self.size = 1
        else:
            parent = self.root
            if(key < self.root.item.key):
                parent.rank +=1
                curr = self.root.left
            else:
                curr = self.root.right
            while (curr is not None):
                parent = curr
                if (key < curr.item.key):
                    curr = curr.left
                    parent.rank += 1
                else:
                    curr = curr.right
            if (key < parent.item.key):
                parent.left = new_node
                parent.rank+=1
                parent.left.rank = 1
            else:
                parent.right = new_node
                parent.right.rank = parent.rank+1
            new_node.parent = parent
            self.size += 1


    #raises exception if key not in tree
    def __delitem__(self, key):
        if (self.subtree_find(self.root, key) is None):
            raise KeyError(str(key) + " is not found")
        else:
            self.subtree_delete(self.root, key)


    #assumes key is in tree + returns value assosiated
    def subtree_delete(self, node, key):
        node_to_delete = self.subtree_find(node, key)
        value = node_to_delete.item.value
        num_children = node_to_delete.num_children()

        if (node_to_delete is self.root):
            if (num_children == 0):
                self.root = None
                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                if (self.root.left is not None):
                    self.root = self.root.left
                    self.root.rank = 1
                else:
                    self.root = self.root.right
                self.root.parent = None
                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                node_to_delete.rank-=1
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        else:
            if (num_children == 0):
                parent = node_to_delete.parent
                if (node_to_delete is parent.left):
                    parent.left = None
                else:
                    parent.right = None

                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                parent = node_to_delete.parent
                if(node_to_delete.left is not None):
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                child.parent = parent
                if (node_to_delete is parent.left):
                    parent.left = child
                else:
                    parent.right = child

                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        return value

    # assumes non empty subtree
    def subtree_max(self, curr_root):
        node = curr_root
        while (node.right is not None):
            node.rank-=1
            node = node.right
        return node

    ######################################## Question 5 ##########################################
    def get_ith_smallest(self, i):
        if i > self.size:
            raise IndexError
        lst = []
        bst_sub_root = self.root
        while True:
            while bst_sub_root is not None:
                lst.append(bst_sub_root)
                bst_sub_root = bst_sub_root.left

            bst_sub_root = lst.pop()

            if i == 1:
                return bst_sub_root.item.key
            else:
                i -= 1
                bst_sub_root = bst_sub_root.right


    def inorder(self):
        for node in self.subtree_inorder(self.root):
            yield node

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)

    def preorder(self):
        for node in self.subtree_preorder(self.root):
            yield node

    def subtree_preorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)

    def __iter__(self):
        for node in self.inorder():
            yield (node.item.key, node.item.value)

########################################## Question 2 ##################################################
def create_chain_bst(n):
    new_bst = BinarySearchTreeMap()
    for num in range(1,n+1):
        new_bst.subtree_insert(num)

    return new_bst

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    if low >= high:
        bst.subtree_insert(low)
        return
    bst.subtree_insert(low+((high-low)//2))
    add_items(bst, low, low+((high-low)//2)-1)
    add_items(bst, low+((high-low)//2)+1, high)

########################################## Question 3 ##################################################
def restore_bst(prefix_lst):
    if len(prefix_lst) == 0:
        return BinarySearchTreeMap()
    else:
        mini = 12342343456453
        for index in range(len(prefix_lst)):
            if mini > prefix_lst[index]:
                mini = prefix_lst[index]
        mini-=1
        maxi = prefix_lst[len(prefix_lst)-1]+1
        restore_bst.index = 0

        def restore_bst_helper(lst, mini, maxi, low, high):
            if len(lst) == 1:
                return BinarySearchTreeMap().Node(BinarySearchTreeMap().Item(lst[low]))
            if low > high:
                return
            if mini < lst[low] < maxi:
                subtree_root = BinarySearchTreeMap().Node(BinarySearchTreeMap().Item(lst[low]))
                restore_bst.index += 1
                if low + 1 < high:
                    subtree_root.left = restore_bst_helper(lst, mini, lst[low], restore_bst.index, high)
                    subtree_root.right = restore_bst_helper(lst, lst[low], maxi, restore_bst.index, high)
                return subtree_root

        bst = BinarySearchTreeMap()
        bst.root = restore_bst_helper(prefix_lst, mini, maxi, 0, len(prefix_lst)-1)
        return bst

########################################## Question 4 ##################################################
def find_min_abs_difference(bst):
    lst = []
    mini = 9999999999
    for node in bst:
        lst.append(node[0])
    for index in range(len(lst)):
        mini = min(mini, abs(lst[index]-lst[index-1]))
    return mini

if __name__=="__main__":
    bst = restore_bst([9,7,3,1,5,13,11,15])
    for node in bst.preorder():
        print(node.item.key, end=" ")

    bst.get_ith_smallest(1)

