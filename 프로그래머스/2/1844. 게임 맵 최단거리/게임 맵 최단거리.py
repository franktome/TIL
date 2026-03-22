from collections import deque

# 완전탐색으로 가야겠는데? - 조금 더 컨트롤하기 쉬운 bfs로 가자.
# distance 행렬 -1로 초기화 하고 거리 업데이트 하자.
# 각 지점에서 최소거리만 계속해서 유지하자. 201이면 못가는 걸로 두자. -1반환 아니면 항상 최솟값을 넣어주자.

def bfs(a,b, n,m, maps, distance):
    q= deque([(a,b)])
    while(q):
        x,y = q.popleft()
        # 종료조건을 넣어줘야 하는구나
        if x==n-1 and y==m-1:
            return
        
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1 and distance[nx][ny]==201:
                distance[nx][ny] = distance[x][y]+1
                q.append((nx,ny))

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    distance = [m*[201] for _ in range(n)]
    distance[0][0]=1
    bfs(0,0, n,m, maps, distance)
    answer = distance[n-1][m-1]
    if answer == 201:
        answer = -1
    return answer