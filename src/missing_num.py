def missing_num(arr):
    """
    Function to find the first missing positive integer in the array.

    :param arr: List of integers
    :return: First missing positive integer
    """
    sorted_arr = [0] * (len(arr)+1)

    for i in range(len(arr)):
        sorted_arr[arr[i] - 1] = arr[i]

    for n in range(len(sorted_arr)):
        if sorted_arr[n] < 1:
            return n + 1

    return 0
