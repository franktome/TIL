from collections import deque

def bfs(m,n, maps, distances, queue):
    while queue:
        x,y = queue.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<m and 0<=ny<n and maps[nx][ny]==1 and distances[nx][ny]==-1:
                distances[nx][ny]=distances[x][y]+1
                queue.append([nx,ny])

def solution(maps):
    m = len(maps)
    n = len(maps[0])
    distances = [[-1]*n for _ in range(m)]
    distances[0][0]=1
    queue = deque([[0,0]])
    bfs(m,n, maps, distances, queue)
    answer = distances[m-1][n-1]
    return answer