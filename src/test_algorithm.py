
import pytest

from src.MyAlgorithm import swap, bubble_sort, quick_sort, merge_sort, inserting_sort, binary_search


class TestAlgorithm:

    def test_swap(self):
        x = 10
        y = 15
        print(x)
        print(y)
        x1, y1 = swap(x, y)
        print(x)
        print(y)
        print(x1)
        print(y1)

    def test_bubble_sort(self):
        nums = [3, 5, 1, 10, -1, 45, 12, 9]
        nums2 = list(nums)
        nums2.sort()
        print(nums)
        bubble_sort(nums)
        print(nums)
        print(nums2)
        assert nums == nums2

    def test_quick_sort(self):
        nums = [3, 5, 1, 10, -1, 45, 12, 9]
        print(nums)
        nums2 = list(nums)
        nums2.sort()
        quick_sort(nums)
        print(nums)
        print(nums2)
        assert nums == nums2

    def test_merge_sort(self):
        nums = [3, 5, 1, 10, -1, 45, 12, 9]
        print(nums)
        nums2 = list(nums)
        nums2.sort()
        merge_sort(nums)
        print(nums)
        print(nums2)
        assert nums == nums2

    def test_inserting_sort(self):
        nums = [3, 5, 1, 10, -1, 45, 12, 9]
        print(nums)
        nums2 = list(nums)
        nums2.sort()
        inserting_sort(nums)
        print(nums)
        print(nums2)
        assert nums == nums2

    def test_binary_search(self):
        nums = [3, 5, 1, 10, -1, 45, 12, 9]
        nums.sort()
        print(nums)
        print(binary_search(nums, 11))
        print(binary_search(nums, -1))
        print(binary_search(nums, 45))
        print(binary_search(nums, 9))



if __name__ == "__main__":
    print("\n\nTest runner launching py.test. Runs all the tests in Tests folder.\n\n")
    pytest.main(['-xvs', 'test_algorithm.py', '-k', 'test_binary_search'])
