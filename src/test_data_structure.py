import pytest

from src.MyDataStructure import LinkedList, BinarySearchTreeNode


class TestDataStructure:


    def test_linked_list_append(self):
        list = LinkedList()
        list.print()
        list.append(3)
        list.append(5)
        list.append(4)
        list.print()

    def test_linked_list_preappend(self):
        list = LinkedList()
        list.append(3)
        list.append(5)
        list.preappend(7)
        list.preappend(1)
        list.print()

    def test_linked_list_delete(self):
        list = LinkedList()
        list.append(3)
        list.append(5)
        list.preappend(7)
        list.preappend(1)
        list.print()
        print("delete element 7")
        list.delete_by_value(7)
        list.print()
        print("delete element 2")
        list.delete_by_value(2)
        list.print()


    def test_binary_search_tree_insert(self):
        b_tree = BinarySearchTreeNode(8)
        b_tree.print_in_order()
        b_tree.insert(3)
        b_tree.insert(5)
        b_tree.insert(10)
        b_tree.insert(9)
        b_tree.print_in_order()


    def test_binary_search_tree_find(self):
        b_tree = BinarySearchTreeNode(8)
        b_tree.print_in_order()
        b_tree.insert(3)
        b_tree.insert(5)
        b_tree.insert(10)
        b_tree.insert(9)
        b_tree.print_in_order()
        print(b_tree.find(5))
        print(b_tree.find(9))
        print(b_tree.find(11))



if __name__ == "__main__":
    print("\n\nTest runner launching py.test. Runs all the tests in Tests folder.\n\n")
    pytest.main(['-xvs', 'test_data_structure.py', '-k', 'test_binary_search_tree_find'])
