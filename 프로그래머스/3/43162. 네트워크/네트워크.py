from collections import deque

def dfs(computers, visited, start):
    stack = deque([start])
    while stack:
        j = stack.popleft()
        if visited[j]==0:
            visited[j]=1
        for i in range(len(computers)):
            if visited[i]==0 and computers[j][i]==1:
                stack.append(i)
    
def solution(n, computers):
    visited=[0]*n
    answer = 0
    i=0
    while 0 in visited:
        if visited[i]==0:
            visited[i]=1
            dfs(computers, visited, i)
            answer+=1
        i+=1
    
    return answer