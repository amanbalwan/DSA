arr=["a","b","c","d"]
#string 4(elements) * 4(for each byte) = 16 bytes

#lookup
print(arr[2]) #O(1)

#push
arr.append("e")

print(arr) #O(1)

#pop

arr.pop() #0(1)

print(arr)

#unshift(add first element )

arr.insert(0,"x") #O(n)

print(arr)

#nosplice in pyhton so insert
arr.insert(2,'hello')
print(arr)