cache={}
def fibonacci(num):
 
    def fib(num1):
        if num1<2:
            return num1
        else:
            if num1-1 not in cache:
                cache[num1-1]=fib(num1-1)
            if num1-2 not in cache:
                cache[num1-2]=fib(num1-2)
            


            return cache[num1-1]+cache[num1-2]
            
    if num in cache:
        print("fast")
        return cache[num]
    else:         
        cache[num]=fib(num)
        return cache[num]
    



print(fibonacci(5))
print(fibonacci(5))
print(fibonacci(8))
print(fibonacci(6))
print(fibonacci(8))
print(fibonacci(100))
print(fibonacci(98))
