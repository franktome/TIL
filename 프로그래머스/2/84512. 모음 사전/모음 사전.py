
def dfs(n,full,lst):
    global full_lst
    if len(lst)==n:
        full_lst.append(lst)
        return
    for i in range(5):
        dfs(n,full,lst+full[i]) # 중복 허욜이기 때문에 따로 visited는 관리하지 않음

full_lst=[]  

def solution(word):
    global full_lst
    for i in range(1,6):
        dfs(i,"AEIOU","")
    final_lst = list(set(full_lst))
    final_lst.sort()
    print(final_lst[:10])
    for idx, x in enumerate(final_lst):
        if word==x:
            return idx+1