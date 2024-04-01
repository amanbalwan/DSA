arr=[2,1,1,2,3,5,1,2,3,4]
def firstrecc(arr):
    dict={}
    for i in arr:
        if i in dict:
            return i
        else:
            dict[i]=1
    return "no element"

print(firstrecc(arr))
