def selectionSort(arr):
    for i in range(len(arr)):
        small=arr[i]
        index=i
        for j in range(i+1,len(arr)):
            if arr[j]<small:
                small=arr[j]
                index=j
        arr[index],arr[i]=arr[i],arr[index]
    return arr



print(selectionSort([99,94,6,2,1,5,63,87,283,34,0]))