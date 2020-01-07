"""
Insertion sort algorithm
worst case: O(nˆ2)
best case: Omega(n)
"""


def insertion_sort(array: list):
    """
    A function that does the insertion sort
    Args:
        array: an unsorted list
    Returns:
        a list of sorted elements
    """

    # loop from 1 to the length of array - 1,
    # using range in python solves the array - 1 issue since the
    # max of range is exclusive
    for i in range(1, len(array)):
        # set a temp to hold the initial value
        temp = array[i]

        # set j to i, so we can use a while loop to check
        j = i

        # while the value in position before temp is greater than the temp
        # and j is the number of shifts we have to do
        val = array[i - 1]
        val_j = array[j - 1]
        while j > 0 and array[j - 1] > temp:
            array[j] = array[j - 1]
            j -= 1

        # then set the position of 0 in the array to the temporary value
        array[j] = temp

    return array


# unsorted_array = [4, 1, 3, 1, 3, 5, 7]
unsorted_array = [5, 2, 1, 3, 6, 4]
sorted_array = insertion_sort(unsorted_array)
print(sorted_array)
