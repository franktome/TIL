import sys
input = sys.stdin.readline
inf = 10e9

n,m = map(int, input().split())
graph = []
for i in range(m):
    a,b,c = map(int, input().split())
    graph.append((a,b,c))
distances = [inf]*(n+1)
distances[1]=0
flag = 0

def bellman_ford():
    global flag
    for i in range(n):
        for j in range(m):
            curr = graph[j][0]
            next = graph[j][1]
            cost = graph[j][2]
            if distances[curr]!=inf and distances[next] > distances[curr] + cost:
                distances[next] = distances[curr]+ cost
                if i==n-1:
                    flag =1

bellman_ford()
if flag==1:
    print(-1)
else:
    for i in range(2,n+1):
        if distances[i]==inf:
            print(-1)
        else:
            print(distances[i])        
