from collections import deque

def bfs(maps, distances, queue):
    n=len(maps)
    m=len(maps[0])
    while(queue):
        x,y = queue.popleft()
        if (x+1<n and distances[x+1][y]==0 and maps[x+1][y]==1):
            distances[x+1][y] = distances[x][y]+1
            queue.append([x+1,y])
        if (y+1<m and distances[x][y+1]==0 and maps[x][y+1]==1):
            distances[x][y+1] = distances[x][y]+1
            queue.append([x,y+1])
        if (x-1>=0 and distances[x-1][y]==0 and maps[x-1][y]==1):
            distances[x-1][y] = distances[x][y] +1
            queue.append([x-1,y])
        if (y-1>=0 and distances[x][y-1]==0 and maps[x][y-1]==1):
            distances[x][y-1] = distances[x][y] +1
            queue.append([x,y-1])
        
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    queue = deque([[0,0]])
    distances = [[0]*m for _ in range(n)]
    distances[0][0] = 1
    
    bfs(maps,distances, queue)
    answer = 0
    if distances[n-1][m-1]==0:
        answer=-1
    else:
        answer=distances[n-1][m-1]
    return answer