import sys
input = sys.stdin.readline
n, m, s = map(int, input().split())

# in_put = input().split()
# in_put = list(map(int,in_put)) # in_put[0],in_put[1],in_put[2]로 사용하면 됨

adj = [[]*(n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for e in adj:
    e.sort()

def dfs(v):
    visited[v] = 1
    print(v)
    for w in adj[v]:
        if not visited[w]:
            dfs(w)

dfs(s)