# 반복문 돌면서 visited관리하고 한 노드에서 bfs로 묶음 계산하고, visited이면 넘어가고
# visited 아닌거 만날때마다 count +1해주고 하면 되지 않을까?
from collections import deque

def bfs(i, n, computers, visited):
    q = deque([i])
    visited[i]=1
    while(q):
        x= q.popleft()
        for k in range(n):
            if computers[x][k]==1 and visited[k]==0:
                q.append(k)
                visited[k]=1

def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        if visited[i]==0:
            answer +=1
            bfs(i, n, computers, visited)
            
    
    return answer