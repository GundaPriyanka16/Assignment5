"Binary Search"

def binary_search(arr,n):
    left = 0 
    right = len(arr) - 1
    mid = 0 
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] < n:
            left = mid + 1 
        elif arr[mid] > n :
            right = mid - 1 
        else:
            return mid 
    return None
arr = [1, 2, -1, 5, 10, 99, 79] 
n = 5 
result = binary_search(arr,n) 
print(result)
