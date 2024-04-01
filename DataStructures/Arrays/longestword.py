def LongestWord(sen):
  maxc=""
  count=""
  for i in sen:
    if i.isalpha():
      count+=i
    elif i == " ":
      maxc=max(maxc,count)
      count=""
    maxc=max(maxc,count)
  return maxc

# keep this function call here 
print(LongestWord(input()))