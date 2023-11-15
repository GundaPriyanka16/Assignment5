"TwoSum" 

def twosum(num, target):
    length = len(num)
    for i in range(length):
        for j in range(i+1, length):
            if n[i] + n[j] == target:
                return [i, j] 
            
n = [3, 1, 1, 5, 8, 25, 76]
target = 8
print(twosum(n,target))
