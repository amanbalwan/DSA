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

q=deque()
seen=[]
q.append(0)

while q:
    current=q.popleft()
    seen.append(current)
    for i in adjecency_list[current]:
        if i not in seen:
            q.append(i)

print(seen)