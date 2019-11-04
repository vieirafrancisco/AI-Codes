import heapq # heap queue to peform an priority queue

def dijkstra(s, t, n, graph):
    if t >= n: return -1
    INF = 99999999
    dist = n*[INF]
    visited = n*[False]
    origin = n*[-1]
    dist[s] = 0
    origin[s] = s
    p_queue = []
    heapq.heappush(p_queue, (0, s))

    while(p_queue != []):
        u = heapq.heappop(p_queue)
        visited[u[1]] = True
        for v in graph[u[1]]:
            if not visited[v[1]] and u[0] + v[0] < dist[v[1]]:
                dist[v[1]] = u[0] + v[0]
                origin[v[1]] = u[1]
                heapq.heappush(p_queue, (dist[v[1]], v[1]))

    if dist[t] == INF: return 0
    return dist[t], origin

if __name__ == '__main__':
    n, m, s, t = map(int, input().split())
    graph = {}

    for i in range(m):
        u, v, c = map(int, input().split())
        if u not in graph.keys(): graph[u] = []
        if v not in graph.keys(): graph[v] = []
        graph[u].append((c, v))
        graph[v].append((c, u))

    print(dijkstra(s, t, n, graph))

    