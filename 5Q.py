"Find the Missing Number" 

def find_missing_number(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list

n_list = input().split() 
n_list = find_missing_number(n_list)
maximum = max(n_list)
num_set = set(n_list)
first_num_set = set(range(1,maximum+1))
missing_num_set = first_num_set.difference(num_set)
missing_n_list = list(missing_num_set)
missing_n_list.sort()
print(missing_n_list)