def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


input_str = input("Enter an array of integers, separated by commas: ")

arr = [int(x) for x in input_str.split(',')]

sorted_arr = quick_sort(arr)

print(sorted_arr)
