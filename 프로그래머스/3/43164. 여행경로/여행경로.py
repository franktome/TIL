from collections import deque

# bfs
# queue에 넣은 다음 다시 정렬해야할 듯!

# bfs -> 임시 list를 만들어서 정렬시킨다음 맨 앞에것만 빼고 나머지는 그냥 버리자.
# q에는 공항명만 관리하자!
# 아 굳이 순서 정렬하지말고 다 만든 다음 정렬시키면 되겠구나. -> dfs로 풀어야 겠는데
# dfs도 일단 입력값 넣기 전에 visited 체크해야되나 아니면 나와서 visited 체크 해야되나...
# 큐에 넣기전에 visited 체크하자.

def dfs(start, n, tickets, visited, tmp, answer):
    # 종료조건
    if len(tmp)== n+1:
        answer.append(tmp)
        return
    for i, ticket in enumerate(tickets):
        if visited[i]==0 and ticket[0]==start:
            visited[i]=1
            dfs(ticket[1], n, tickets, visited, tmp+[ticket[1]], answer)
            visited[i]=0
# dfs는 재귀로 내린다는 느낌 
# 초반에는 종료조건 적어주면 될듯!
# -> 여러갈래로 가고 싶다면 visited 닫았다 여는 거 신경쓰기
            
def solution(tickets):
    answer = []
    n = len(tickets)
    visited = [0]*n
    
    tmp = ["ICN"]
    dfs("ICN", n, tickets, visited, tmp, answer)
    answer.sort()
    return answer[0]