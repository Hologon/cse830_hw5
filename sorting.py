import random


def insertion_sort(array):
    for i in range(1, len(array)):
        val = array[i]

        j = i-1
        while j >= 0 and val < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = val


# Merge sort implementation from
# https://www.educative.io/answers/merge-sort-in-python
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1

            k += 1

        # For all the remaining values
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def hybrid_sort(array, threshold):
    if len(array) <= threshold:
        insertion_sort(array)
        return

    if len(array) <= 1:
        return

    # Merge sort otherwise
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # Recursive call on each half
    hybrid_sort(left, threshold)
    hybrid_sort(right, threshold)

    # Two iterators for traversing the two halves
    i = 0
    j = 0

    # Iterator for the main list
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

        k += 1

    # For all the remaining values
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


def test_sort(sort_func, n, threshold=None):
    data = list(range(n))
    random.shuffle(data)
    if threshold is None:
        sort_func(data)
    else:
        sort_func(data, threshold)
