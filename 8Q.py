"Merge Intervals"

def merge(arr, l):
    arr.sort()
    i = 0
    while i < l - 1:
        if arr[i][0] == arr[i + 1][0] and arr[i][1] == arr[i + 1][1]:
            i += 1
            continue
        a = []
        for n in range(arr[i][0], 1 + arr[i][1]):
            a.append(n)
        for n in range(arr[i + 1][0], 1 + arr[i + 1][1]):
            if n in a:
                new_pair = [min(arr[i][0], arr[i + 1][0]), max(arr[i][1], arr[i + 1][1])]
                arr[i] = new_pair
                arr[i + 1] = new_pair
                i = 0
                break
        i += 1
    ans = []
    for i in arr:
        if i not in ans:
            ans.append(i)
    return ans


arr = [[1, 4], [2, 5], [11, 10], [15, 17], [18, 20]]
l = len(arr)
print(merge(arr, l))