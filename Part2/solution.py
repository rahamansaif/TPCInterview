"""Code to find the maximum sum subarray of a given array.
"""

def max_sum_subarray(arr):
    global_max = float('-inf')
    current_sum = 0
    for n in arr:
        if current_sum < 0:
            current_sum = n
        else:
            current_sum += n
        if current_sum > global_max:
            global_max = current_sum
    return global_max


# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(max_sum_subarray(arr))
