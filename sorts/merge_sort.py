"""
Merge sort algorithm
worst case: O(nˆ2)
best case: Omega(n)
"""


def merge_sort(array: list):
    """
    A function that does the merge sort
    Args:
        array: an unsorted list
    Returns:
        a list of sorted elements
    """

    # check if the list is not empty and is greater than one element
    if len(array) > 1:
        # get the middle of the list, do an integer division, we don't need decimals
        # assign a left part and a right part
        middle = len(array) // 2
        left_half = array[:middle]
        right_half = array[middle:]

        # call merge_sort recursively to keep dividing the list
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0  # used to track left half of the list
        j = 0  # used to track right side of the list
        k = 0  # used to track the array itself

        # merge both left and right part of the list
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        # merge the left half in an ordered fashion
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        # merge the right half in an ordered fashion
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array


# unsorted_array = [4, 1, 3, 1, 3, 5, 7]
unsorted_array = [5, 2, 1, 3, 6, 4]
# unsorted_array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sorted_array = merge_sort(unsorted_array)
print(sorted_array)
