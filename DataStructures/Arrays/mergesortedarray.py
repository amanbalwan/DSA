def mergeSortedArrays(arr1,arr2):
    a1=0
    a2=0
    l1=len(arr1)
    l2=len(arr2)
    arr3=[]
    if l1 == 0:
        return arr2
    if l2 == 0:
        return arr1
    for i in range(0,l1+l2):
        if a1== l1-1:
            arr3.extend(arr2[a2:])
            break
        elif a2== l2-1:
            arr3.extend(arr1[a1:])
            break
        elif arr1[a1]<=arr2[a2]:
            arr3.append(arr1[a1])
            a1+=1
        else:
            arr3.append(arr2[a2])
            a2+=1
    return arr3




    

print(mergeSortedArrays([],[]))