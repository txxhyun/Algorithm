def dfs(v):
    visited[v] = True # 정점 v 방문
    print(v, end=' ') # 정점 v 출력
    for w in adj_list[v]: # 정점 v에 인접한 각 정점에 대해
        if not visited[w]: 
            dfs(w) # v에 인접한 방문 안된 정점 재귀호출

adj_list = [[-1], [2, 3, 4, 6], [1, 4, 5,7], [1, 6], 
            [1, 2, 7], [2,7], [1,3,7], [2,4,5,8], [7]] 
N = len(adj_list) 
visited = [0 for x in range(N+1)] #false == 0

print('[DFS 방문 순서]')     
in_ver = int(input('시작 정점 => '))
dfs(in_ver)
