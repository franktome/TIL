from collections import deque

def solution(n, edge):
    distances=[-1]*(n+1)
    distances[1]=0
    graph=[[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    queue=deque([1])
    
    while(queue):
        start = queue.popleft()
        for end in graph[start]:
            if distances[end]==-1 :
                distances[end] = distances[start]+1
                queue.append(end)
    M = max(distances)
    answer = distances.count(M)
    return answer