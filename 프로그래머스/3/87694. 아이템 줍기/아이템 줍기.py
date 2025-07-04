from collections import deque

def bfs(queue, graph, distances, itemx, itemy):
    while(queue):
        x,y = queue.popleft()
        if x==itemx and y==itemy:
            break
        for dx, dy in [(0,-1),(0,1),(-1,0),(1,0)]:
            nx, ny = x+dx, y+dy
            if 0<nx<101 and 0<ny<101 and graph[nx][ny]==1 and distances[nx][ny]==-1:
                distances[nx][ny] = distances[x][y]+1
                queue.append([nx, ny])

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 인접한 지점에서 선으로 연결된 부분이 아닌데 건너뛸 수 있는 부분을 아예 맴 자체를 2배로 해서 풀이한 아이디어는 가져가자!
    graph = [[-1]*102 for _ in range(102)]
    distances = [[-1]*102 for _ in range(102)]
    
    for r in rectangle:
        x1,y1,x2,y2 = map(lambda x:2*x, r) 
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                # 내부를 0으로 채워서 테두리만 남기는 아이디어도 좋다.
                if x1<i<x2 and y1<j<y2:
                    graph[i][j]=0
                # 그래프 영역을 3부분으로 나누는 아이디어가 좋다.
                # 다른 직사각형의 내부라면 무시하고 직사각형의 내부가 아니라면 1로 표시하기
                elif graph[i][j]!=0:
                    graph[i][j]=1
    distances[characterX*2][characterY*2]=0
    queue = deque([[characterX*2,characterY*2]])
    bfs(queue, graph, distances, itemX*2, itemY*2)
                    
    answer = distances[itemX*2][itemY*2]/2
    return answer