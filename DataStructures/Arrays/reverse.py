def reverse(str1):
    print("The original string is:","\n",str1)
    if str1 is None or len(str1)<2:
        return str1

    a=""
    for i in str1[::-1]:
        a+=i
    return a

str1 = "Hello I am Aman, from Mumbai, 410210" 
print(reverse(str1))

