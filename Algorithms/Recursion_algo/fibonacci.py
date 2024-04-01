def fibonacciRecursive(index):
    if index<2:
        return index
    return fibonacciRecursive(index-1)+fibonacciRecursive(index-2)

#def fibonacciIterative(index):
    if index==0:
        return 0
    elif index==1 or index==2:
        return 1
    else:
        prev=1
        sum=1
        for i in range(2,index):
            prev,sum=sum,prev+sum
        return sum

def fibonacciIterative(index):
    arr=[0,1]
    for i in range(2,index+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[index]

print(fibonacciRecursive(21))
print(fibonacciIterative(21))