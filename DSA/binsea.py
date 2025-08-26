def binary_search(arr, x):

    low = 0
    high = len(arr) - 1

    while (low <= high):
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

    return -1

arr = [2, 3, 10, 40, 50]
x = 40

result = binary_search(arr, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")