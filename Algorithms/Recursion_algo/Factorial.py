def findFactorialRecursion(number):
    if number==1:
        return 1
    return number*findFactorialRecursion(number-1)


def findFactorialItertive(number):
    fac=1
    while(number>1):
        fac=fac*number
        number-=1
    return(fac)

print(findFactorialRecursion(19))
print(findFactorialItertive(19))