def dfs(graph, queue, route):
    while(queue):
        start = queue[-1]
        if start not in graph or len(graph[start])==0:
            route.append(queue.pop())
        else:
            queue.append(graph[start].pop())

def solution(tickets):
    graph={}
    for t in tickets:
        if t[0] in graph:
            graph[t[0]].append(t[1])
        else:
            graph[t[0]] = [t[1]]
    for t in graph:
        graph[t].sort(reverse=True)
    queue= ["ICN"]
    route = []
    dfs(graph, queue, route)

    return route[::-1]