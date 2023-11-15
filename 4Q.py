"FizzBuzz" 

def  fizz_buzz(n):
    if (n % 3 ==0) and (n % 5 == 0):
        result = "FizzBuzz"
    elif (n % 3 == 0):
        result = "Fizz"
    elif (n % 5 == 0):
        result = "Buzz"
    else:
        result = n 
    return result

n = int(input()) 
result = fizz_buzz(n=n)
print(result)