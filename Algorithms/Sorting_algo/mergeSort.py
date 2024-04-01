def mergeSort(arr):
    if len(arr)==1:
        return arr

    return merge(mergeSort(arr[:len(arr)//2]),mergeSort(arr[len(arr)//2:]))

def merge(arr1,arr2):
    arr=[]
    i=0 
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    if i == len(arr1):
        arr.extend(arr2[j:])
    else:
        arr.extend(arr1[i:])
    return arr


print(mergeSort([99,94,6,2,1,5,63,87,283,34,0]))