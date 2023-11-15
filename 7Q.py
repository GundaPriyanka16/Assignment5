"Maximum Subarray Sum"

def maxSubArraySum(arr, s): 
    max_t = arr[0] 
    max_e = 0 
    for i in range(0,s):
        max_e = max_e + arr[i]
        if max_e < 0: 
            max_e = 0 
        elif (max_t < max_e):
            max_t = max_e 
    return max_t 
arr = [-2, -1, -3, 4, 5, -3, -2]
print(maxSubArraySum(arr, len(arr)))
        