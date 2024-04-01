def insertionSort(arr):
    for i in range(1,len(arr)):
        j=i
        while(j>0 and arr[j]<arr[j-1]):
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    return arr
        
            
        


print(insertionSort([99,94,6,2,1,5,63,87,283,34,0]))