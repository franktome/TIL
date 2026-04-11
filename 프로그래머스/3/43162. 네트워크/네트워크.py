from collections import deque

def bfs(start, n, computers, visited):
    q=deque([start])
    visited[start]=1
    while(q):
        x = q.popleft()
        for i in range(n):
            if visited[i]==0 and computers[x][i]==1:
                q.append(i)
                visited[i]=1

def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        if visited[i]==0:
            bfs(i, n, computers,visited)
            answer+=1
    return answer