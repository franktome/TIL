from math import sqrt

def dfs(numbers, visited, n, lst):
    global all_lst
    if len(lst)==n:
        all_lst.append(int(lst))
        return
    idx_lst = [idx for idx,x in enumerate(visited) if x==0]
    for i in idx_lst:
        visited[i]=1
        dfs(numbers, visited,n,lst+numbers[i])
        visited[i]=0
def check(k):
    for i in range(2,int(sqrt(k))+1):
        if k%i==0:
            return False
    return True
        
all_lst = []
def solution(numbers):
    global all_lst
    visited = [0]*len(numbers)
    for n in range(1,len(numbers)+1):
        dfs(numbers, visited, n, "")
    final_lst = list(set(all_lst))
    count=0
    for i in final_lst:
        if i>=2 and check(i) :
            count+=1
        
    return count