"Anagram check" 

a = input() 
b = input() 
if sorted(a) == sorted(b):
    print("strings are anagram")
else: 
    print("strings are not anagram")