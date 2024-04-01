def bubbleSort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr



print(bubbleSort([99,94,6,2,1,5,63,87,283,34,0]))