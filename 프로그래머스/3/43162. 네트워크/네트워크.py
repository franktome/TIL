from collections import deque

def dfs(n, computers, visited, start):
    queue=deque([start])
    while queue:
        a=queue.popleft()
        visited[a]=1
        for idx,b in enumerate(computers[a]):
            if visited[idx]==-1 and b==1:
                queue.append(idx)

def solution(n, computers):
    answer = 0
    visited = [-1]*n
    for i in range(n):
        if visited[i]==-1:
            dfs(n,computers, visited, i)
            answer+=1
    return answer