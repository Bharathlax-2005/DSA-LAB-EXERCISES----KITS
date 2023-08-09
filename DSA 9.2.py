def linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


i_str = (input("enter"))
arr = [int(x) for x in i_str.split(',')]
target = int(input("enter target:"))

index = linear(arr, target)
if index < 1:
    print(f"{target} not found in array")
else:
    print(f"{target} found at index{index}")
