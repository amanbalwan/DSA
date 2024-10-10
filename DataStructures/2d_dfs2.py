testMatrix = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20]
]
row=len(testMatrix)
column=len(testMatrix[0])

directions=[
    [-1,0],
    [0,1],
    [1,0],
    [0,-1]
]
values=[]
visited=[['f' for _ in range(column)] for _ in range(row)]

def finding_element(r,c):
    if r<0 or r>=row or c<0 or c>=column or visited[r][c] == 't':
        return 
    if visited[r][c] =='f':
        visited[r][c]='t'
        values.append(testMatrix[r][c])
    for i in directions:
        finding_element(r+i[0],c+i[1])

finding_element(0,0)
print(values)

