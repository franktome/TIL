from collections import deque

def compare(a,b):
    count=0
    for i in range(len(a)):
        if a[i] != b[i]:
            count+=1
    if count!=1:
        return 0
    else:
        return 1

def bfs(target, words, distances, queue):
    while(queue):
        a = queue.popleft()
        if a==target:
            return
        for b in words:
            if compare(a,b) and distances[b]==0:
                distances[b] = distances[a]+1
                queue.append(b)
            
def solution(begin, target, words):
    queue = deque([begin])
    # distances 딕셔너리로 관리해야 겠다.
    print(target)
    distances = {a:0 for a in words}
    distances[begin]=0
    print(distances)
    if target not in words:
        return 0
    bfs(target, words, distances, queue)
    
    answer = 0
    answer = distances[target]
    return answer