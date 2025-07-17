def get_second_largest(arr):
    # Code Here
    if arr is None or len(arr) < 2:
        return -1

    sorted_arr = sorted(arr, reverse=True)
    for n in sorted_arr[1:]:
        if n < sorted_arr[0]:
            return n

    return -1
