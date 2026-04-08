import sys
import heapq
input = sys.stdin.readline
inf = 10e9

v,e = map(int, input().split())
s = int(input())
graph = [[] for _ in range(v+1)]
distances = [inf for _ in range(v+1)]
distances[s]=0

for i in range(e):
    a,b,w= map(int, input().split())
    graph[a].append((w,b))

def dijkstra(start, graph, distances):
    q=[]
    heapq.heappush(q,(0,start)) # 여기서 heap에 넣어주는 값 중에서 첫 번쩨 값은 distance의 가중치를 의미하네. 이걸로 정렬해야 해서 distance가 있음에도 다시 넣어주네.
    while(q):
        w, n = heapq.heappop(q)
        for w2,n2 in graph[n]:
            if distances[n2]> distances[n]+w2:
                distances[n2] = distances[n]+w2
                heapq.heappush(q,(distances[n]+w2,n2))

dijkstra(s,graph,distances)
for i in range(1,v+1):
    if distances[i]==inf:
        print("INF")
    else:
        print(distances[i])
