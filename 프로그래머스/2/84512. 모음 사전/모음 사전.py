
def dfs(visited,n,full,lst):
    global full_lst
    if len(lst)==n:
        full_lst.append(lst)
        return
    for i in range(5):
        dfs(visited,n,full,lst+full[i])

full_lst=[]  

def solution(word):
    global full_lst
    visited = [0]*5
    for i in range(1,6):
        dfs(visited,i,"AEIOU","")
    final_lst = list(set(full_lst))
    final_lst.sort()
    print(final_lst[:10])
    for idx, x in enumerate(final_lst):
        if word==x:
            return idx+1