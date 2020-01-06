"""
Selection sort algorithm
worst case: O(nˆ2)
best case: Omega(nˆ2)
"""


def selection_sort(array: list):
    """
    A function that does the selection sort
    Args:
        array: an unsorted list
    Returns:

    """
    # loop through the list
    for i in range(len(array)):
        # set the index of the first element
        minimum_index = i

        # loop through a new list from minimum_index + 1 to the end of the unsorted array
        # and check for the smallest in the new list
        for j in range(minimum_index + 1, len(array)):
            if array[minimum_index] > array[j]:
                minimum_index = j

        # swap the found minimum element with the first element in the unsorted array
        array[i], array[minimum_index] = array[minimum_index], array[i]
    return array


# unsorted_array = [4, 1, 3, 1, 3, 5, 7]
unsorted_array = [5, 2, 1, 3, 6, 4]
sorted_array = selection_sort(unsorted_array)
print(sorted_array)
