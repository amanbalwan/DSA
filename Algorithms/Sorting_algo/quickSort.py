def quickSort(arr):
    left=0
    right=len(arr)-1

    if len(arr) <= 1:  
        return arr

    if len(arr)==2:
        if arr[right]<arr[left]:
            arr[right],arr[left]=arr[left],arr[right]
        return arr
    
    while(left<right):
        if arr[right]<arr[left]:
            arr[right],arr[left],arr[right-1]=arr[left],arr[right-1],arr[right]
            right-=1
        else:
            left+=1

    return quickSort(arr[:right])+[arr[right]]+quickSort(arr[right+1:])

print(quickSort([99,94,6,2,1,5,63,87,283,34,0]))
print(quickSort([-5, -10, -3, -8, -1]))
print(quickSort([3, 2, 1, 2, 3]))
import random
random.seed(42)  # Setting seed for reproducibility
array = [random.randint(0, 1000) for _ in range(100)]
print(quickSort(array))


