import sys
input = sys.stdin.readline
inf = 10e9

r,c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(input().strip()))

dist = [(-1,0),(1,0),(0,-1),(0,1)]

def dfs(a,b, graph, count):
    global best_count
    best_count = max(count, best_count)

    for dx,dy in dist:
        nx = a+dx
        ny = b+dy
        if 0<=nx<r and 0<=ny<c: 
            if graph[nx][ny] not in visited:
                visited.add(graph[nx][ny])
                dfs(nx,ny, graph, count+1)
                visited.remove(graph[nx][ny])

visited = set()  
visited.add(graph[0][0])
best_count=0 
dfs(0,0,graph, 1)
print(best_count)
