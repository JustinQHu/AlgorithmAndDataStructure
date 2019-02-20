"""
Node definition of List
"""


class LinkNode:
    def __init__(self, data):
        self.data = data
        self.next = None


"""
implementation of LinkedList
"""


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        if not self.head:
            self.head = LinkNode(data)
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = LinkNode(data)

    def preappend(self, data):
        if not self.head:
            self.head = LinkNode(data)
            return
        new_head = LinkNode(data)
        new_head.next = self.head
        self.head = new_head


    def delete_by_value(self,data):
        if self.head.data == data:
            self.head = self.head.next
            return

        index = self.head
        while index.next:
            if index.next.data == data:
                index.next = index.next.next
                return
            index = index.next


    def print(self):
        if not self.head:
            print(None)
            return
        index = self.head
        print()
        while index:
            print("{} -> ".format(index.data))
            index = index.next

"""
binary search tree implementation by recursive methods
"""


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data <= self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def find(self, data):
        if data == self.data:
            return True
        elif data < self.data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False


    def print_in_order(self):
        if self.left:
            self.left.print_in_order()

        print(self.data)

        if self.right:
            self.right.print_in_order()




"""
Node definition for binary tree 
"""


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



"""
binary search tree implementation in iterater way
"""
class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = BinaryTreeNode(data)
            return

        index_node = self.root

        while index_node:
            if data < index_node.data:
                index_node = index_node.left
            elif data > index_node.data:
                index_node = index_node.right
            else:
                return

        index_node = BinaryTreeNode(data)
        return

    def find(self, data):
        pass

    def print_in_order(self):
        pass
