def binary(arr,target):
    left=0
    right=len(arr)-1
    while left <= right:
        mid=(left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return -1
i_str=(input("enter"))
arr=[int(x) for x in i_str.split(',')]
target=int(input("enter target:"))

index=binary(arr,target)
if index < 1:
    print(f"{target} not found in array")
else:
    print(f"{target} found at index{index}")
