"""
Some basic Algorithms in Python
"""

"""
swap two nums
"""


def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y


"""
bubble sort
:type nums: List[int] or List[float]
"""


def bubble_sort(nums):
    length = len(nums)
    i = 0
    while i < length - 1:
        j = 0
        while j < length - 1 - i:
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = swap(nums[j],  nums[j + 1])
            j = j + 1
        i = i + 1


def partition(nums, start_index, end_index):
    pivot_index = int((start_index + end_index)/2)
    pivot = nums[pivot_index]
    i = start_index
    j = end_index
    while i < j:
        while i <= end_index:
            if nums[i] < pivot:
                i = i + 1
            else:
                break

        while j >= start_index:
            if nums[j] > pivot:
                j = j - 1
            else:
                break

        if i < j:
            nums[i], nums[j] = swap(nums[i], nums[j])

    return i


"""
quick sort on sub array
"""


def quick_sort_implement(nums, i, j):
    if i >= j:
        return
    partition_index = partition(nums, i, j)
    quick_sort_implement(nums, i, partition_index)
    quick_sort_implement(nums, partition_index + 1, j)


"""
quick sort
:type nums: List[int] or List[float]
"""


def quick_sort(nums):
    quick_sort_implement(nums, 0, len(nums) - 1)



"""
merge sort
:type nums: List[int] or List[float]
"""


def merge_sort(nums):
    temp_array = [None] * len(nums)
    merge_sort_implement(nums, temp_array, 0, len(nums) - 1)
    

"""
implementation of merge sort
"""


def merge_sort_implement(nums, temp_array, left, right):
    if left >= right:
        return
    mid = int((left + right) / 2)
    merge_sort_implement(nums, temp_array, left, mid)
    merge_sort_implement(nums, temp_array, mid + 1, right)
    merge_halves(nums, temp_array, left, mid, right)


"""
merge the two halves that have been sorted
"""


def merge_halves(nums, temp_array, left, mid, right):
    left_start = left
    left_end = mid
    right_start = mid + 1
    right_end = right
    temp_index = left

    while left_start <= left_end and right_start <= right_end:
        if nums[left_start] < nums[right_start]:
            temp_array[temp_index] = nums[left_start]
            left_start = left_start + 1
        else:
            temp_array[temp_index] = nums[right_start]
            right_start = right_start + 1

        temp_index = temp_index + 1

    while left_start <= left_end:
        temp_array[temp_index] = nums[left_start]
        temp_index = temp_index + 1
        left_start = left_start + 1

    while right_start <= right_end:
        temp_array[temp_index] = nums[right_start]
        temp_index = temp_index + 1
        right_start = right_start + 1

    i = left
    while i <= right_end:
        nums[i] = temp_array[i]
        i = i + 1



"""
inserting sort
"""


def inserting_sort(nums):
    length = len(nums)
    i = 1
    while i < length:
        j = i
        while j > 0:
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = swap(nums[j], nums[j - 1])
                j = j - 1
            else:
                break
        i = i + 1


"""
binary search 
nums should be ascending sorted
"""


def binary_search(nums, key):
    length = len(nums)
    return binary_search_for_range(nums, key, 0, length - 1)


def binary_search_for_range(nums, key, start, end):
    if start > end:
        return -1

    mid = int((start + end) / 2)
    if key == nums[mid]:
        return mid
    elif key < nums[mid]:
        return binary_search_for_range(nums, key, start, mid - 1)
    else:
        return binary_search_for_range(nums, key, mid + 1, end)
