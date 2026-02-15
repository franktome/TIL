from collections import deque

def bfs(numbers, target):
    q= deque([(0,0)])
    answer=0
    while q:
        current_sum, index = q.popleft()
        
        if index == len(numbers):
            if current_sum==target:
                answer+=1
        else:
            q.append((current_sum + numbers[index], index+1))
            q.append((current_sum - numbers[index], index+1))
    return answer
                
def solution(numbers, target):
    return bfs(numbers, target)