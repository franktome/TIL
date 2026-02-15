import sys
sys.setrecursionlimit(3000)

def dfs(x,y,m,graph,visited,tmp, event):
        visited[x][y]=1
        tmp.append([x,y])
        for d_x, d_y in ([0,1], [0,-1],[-1,0],[1,0]):
            n_x, n_y = x + d_x, y + d_y
            if 0<=n_x<m and 0<=n_y<m:
                if visited[n_x][n_y]==0 and graph[n_x][n_y]==event:
                    dfs(n_x, n_y,m,graph,visited,tmp,event)
                
def optimize(tmp_lst):
    x_min = min(x[0] for x in tmp_lst)
    y_min = min(x[1] for x in tmp_lst)
    new_lst = sorted([[x-x_min,y-y_min] for x,y in tmp_lst])
    return new_lst

def rotate(tmp_lst,m):
    new_lst = [[y,m-1-x] for x,y, in tmp_lst]
    return optimize(new_lst)

def solution(game_board, table):
    m = len(game_board)
    block_lst = []
    blank_lst = []
    
    # block 찾기
    block_visited=[[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if table[i][j]==1 and block_visited[i][j]==0:
                tmp = []
                dfs(i, j, m, table, block_visited, tmp, 1)
                block_lst.append(optimize(tmp))
    
    # blank 찾기
    blank_visited = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if game_board[i][j]==0 and blank_visited[i][j]==0:
                tmp = []
                dfs(i, j, m, game_board, blank_visited, tmp, 0)
                blank_lst.append(optimize(tmp))
    
    # blank 돌면서 block 맞춰보기
    count = 0
    block_count = len(block_lst)
    block_use = [False] * block_count
    
    for blank in blank_lst:
        for i in range(block_count):
            match = False
            if block_use[i]==True or len(blank)!=len(block_lst[i]):
                continue
                
            curr_block = block_lst[i]
            for _ in range(4):
                if blank==curr_block:
                    block_use[i]=True
                    count+=len(curr_block)
                    match = True
                    break
                else:
                    curr_block = rotate(curr_block,m)
            if match==True:
                break
    return count