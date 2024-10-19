from collections import deque


adjecency_list=[
    [1,3],
    [0],
    [3,8],
    [0,2,4,5],
    [3,6],
    [3],
    [4,7],
    [6],
    [2]
    ]


if not adjecency_list:
    exit

qu=deque()
seen=[]
qu.append(0)




def dfs(q):
    while q:
        current=q.popleft()  
        seen.append(current)
        for i in adjecency_list[current]:
           if i not in seen:
            q.append(i)
            dfs(q)
            

dfs(qu)
print(seen)



