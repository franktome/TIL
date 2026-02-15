def dfs(x,visited, n, computers):
    visited[x] = True
    for i in range(n):
        if visited[i]==False and computers[x][i]==1:
            dfs(i,visited,n, computers)
    

def solution(n, computers):
    answer = 0
    visited = n*[False]
    for i in range(n):
        if visited[i]==False:
            dfs(i, visited,n, computers)
            answer+=1
    return answer