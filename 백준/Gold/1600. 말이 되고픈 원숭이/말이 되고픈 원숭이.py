# 말처럼 가는 방법을 썼는지 안 썼는지 관리하는 변수(조건 하나 달기)
# 아님 그냥 사방으로 가기
# bfs로 가야겠는걸?
# dfs로 가야된다.

import sys
from collections import deque
input = sys.stdin.readline
inf = 10e9

k = int(input())
w,h = map(int,input().split())
graph=[]
for i in range(h):
    graph.append(list(map(int,input().split())))

dist = [[1,0],[0,1],[-1,0],[0,-1]]
horse = [[-2,-1], [-2,1],[-1,-2],[-1,2],[2,-1],[2,1],[1,-2],[1,2]]

def bfs():
    visited = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]
    queue = deque()
    queue.append([0,0,0])
    visited[0][0][0] = 1

    while queue:
        x,y,z = queue.popleft()

        if x==h-1 and y==w-1:
            return visited[x][y][z]-1
        
        if z<k:
            for (hi, hj) in horse:
                hx, hy = x+hi, y+hj
                if 0<=hx<h and 0<=hy<w:
                    if not graph[hx][hy]:
                        # z+1번째 말처럼 이동하는 중
                        if not visited[hx][hy][z+1]:
                            visited[hx][hy][z+1] = visited[x][y][z]+1
                            queue.append([hx,hy,z+1])

        for (i,j) in dist:
            dx, dy = x+i, y+j
            if 0<=dx<h and 0<=dy<w and not visited[dx][dy][z] and not graph[dx][dy]:
                visited[dx][dy][z] = visited[x][y][z]+1
                queue.append([dx,dy,z])
    return -1

print(bfs())