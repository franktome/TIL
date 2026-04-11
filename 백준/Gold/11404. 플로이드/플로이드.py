import sys
input = sys.stdin.readline
inf = 10e9

n = int(input().strip())
m = int(input().strip())
graph = [[inf]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a][b]=min(graph[a][b],c)

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

def bellman_ford():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][j]> graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

bellman_ford()
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == inf:
            print(0,end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

        
