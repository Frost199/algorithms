"""
Bubble sort algorithm
worst case: O(nˆ2)
best case: Omega(n)
"""


def bubble_sort(array: list):
    """
    A function that does bubble sort
    Args:
        array: an unsorted list

    Returns:
        a list of sorted elements
    """

    # set a swap counter
    swap_counter = 1

    # as long as swap counter is not zero, do a swap
    while swap_counter != 0:
        swaps_done = 0
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                # swap the numbers
                array[i], array[i + 1] = array[i + 1], array[i]
                swaps_done += 1
        swap_counter = swaps_done
    return array


unsorted_array = [5, 2, 1, 3, 6, 4]
# unsorted_array = [2, 7, 6, 3, 1, 5, 4, 10, 32, 4, 40, 20, 32, 100, 23, 18]
sorted_array = bubble_sort(unsorted_array)
print(sorted_array)
