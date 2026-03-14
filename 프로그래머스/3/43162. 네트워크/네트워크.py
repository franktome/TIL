from collections import deque

def bfs(start,visited,n,computers):
    q = deque([start])
    visited[start]=True
    while q:
        network = q.popleft()
        for index, value in enumerate(computers[network]):
            if visited[index]==False and value==1:
                q.append(index)
                visited[index]=True
        
def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if visited[i]==False:
            bfs(i, visited, n, computers)
            answer+=1
    return answer