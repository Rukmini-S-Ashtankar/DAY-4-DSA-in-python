def binarySearch(array, target):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (low+high)//2             #// is used so that the divisiion does not give answer in decimals.
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid+1
        else:
            low = mid-1
    return -1

array = [2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]
target = 72
result = binarySearch(array, target)
if result == -1:
    print("Element not found")
else:
    print("Element found at", result)