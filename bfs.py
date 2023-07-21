def bfs(i):
    queue = [] # 큐 선언 (리스트로 큐 구현)
    visited[i] = True
    queue.append(i) # 큐에 시작정점 삽입        
    while len(queue) != 0: 
        v = queue.pop(0) # 큐에서 정점 v를 가져옴 
        print(v, end=' ') # 정점 v 출력
        for w in adj_list1[v]: # 정점 v에 인접한 방문 안된 정점에 대해
            if not visited[w]: 
                visited[w] = True
                queue.append(w) # v에 인접한 정점을 큐에 삽입


adj_list = [[-1], [2, 3, 4, 6], [1, 4, 5,7], [1, 6], 
            [1, 2, 7], [2,7], [1,3,7], [2,4,5,8], [7]]

adj_list1 = [[1,2,3],[0,4],[0,4,5],[0,5],[1,2,6],[2,3,6],[4,5]]
N = len(adj_list1) 
visited = [False for x in range(N+1)]

print('[BFS 방문 순서]')     
in_ver = int(input('시작 정점 => '))
bfs(in_ver)
