from collections import deque

def bfs(n,m,visited, maps):
    q=deque([(0,0)])
    visited[0][0]=1
    while(q):
        x,y = q.popleft()
        if x==n-1 and y==m-1:
            return
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx= x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1 and visited[nx][ny]==201:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
                
def solution(maps):
    n= len(maps)
    m = len(maps[0])
    visited = [[201]*m for _ in range(n)]
    
    bfs(n,m,visited, maps)
    if visited[n-1][m-1]==201:
        return -1
    else:
        return visited[n-1][m-1]