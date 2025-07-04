from collections import deque

def check(a,b):
    n=len(a)
    count=0
    for i in range(n):
        if a[i]!=b[i]:
            count+=1
    if count==1:
        return True
    return False

def bfs(target, words, distances, queue):
    while(queue):
        a=queue.popleft()
        if a==target:
            return
        for b in words:
            if check(a,b) and distances[b]==-1:
                distances[b]=distances[a]+1
                queue.append(b)
    

def solution(begin, target, words):
    distances={}
    for word in words:
        distances[word]=-1
    distances[begin]=0
    distances[target]=-1
    queue = deque([begin])
    bfs(target, words, distances, queue)
    answer=0
    if distances[target]!=-1:
        answer=distances[target]
    return answer