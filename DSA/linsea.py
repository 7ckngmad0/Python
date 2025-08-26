def linsea(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target is not found in the list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linsea(numbers, 12)
verify(result)

result = linsea(numbers, 6)
verify(result)