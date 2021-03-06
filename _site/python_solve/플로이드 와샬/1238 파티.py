# 입력 및 무한대 그래프 설정.
n, m, x = map(int, input().split())
INF = 987654321
graph = [[INF for i in range(n)]for j in range(n)]

# 방향 입력 가중치 설정.
for i in range(m):
    x, y, v = map(int, input().split())
    graph[x-1][y-1] = v

# 자시자신으로는 못감.
for i in range(n):
    graph[i][i] = 0

# 플로이드
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 2로 가서 2에서 돌아오는게 무조건 가능.
# 가능한것들중에 최대값 설정.
ret = 0
for i in range(n):
    ret = max(ret, graph[i][v] + graph[v][i])

# 출력
print(ret)