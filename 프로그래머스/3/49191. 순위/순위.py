# 이걸 플로이드 워셜로 풀다니.. 정말로 신기하네

def solution(n, results):
    graph = [[0]*(n+1) for _ in range(n+1)]
    for a,b in results:
        graph[a][b]=1
        graph[b][a]=-1
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][k]==graph[k][j]==1:
                    graph[i][j]=1
                    graph[j][i]=graph[k][i]=graph[j][k]=-1
    answer=0
    for i in range(1,n+1):
        if graph[i].count(0)==2:
            answer+=1
    return answer