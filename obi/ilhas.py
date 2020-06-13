from heapq import heappush, heappop
import sys
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    i1, i2, ping = map(int, sys.stdin.readline().split())
    i1-=1
    i2-=1
    graph[i1].append((i2, ping))
    graph[i2].append((i1, ping))

server = int(input())
server-=1

dist = [None] * n
dist[server] = 0

maxPing = None
minPing = None

heap = []
heappush(heap, (dist[server], server))

while len(heap) > 0:
    d, u = heappop(heap)
    if dist[u] < d:
        continue

    if u != server:
        if minPing is None or minPing > dist[u]:
            minPing = dist[u]
        if maxPing is None or maxPing < dist[u]:
            maxPing = dist[u]

    for vertex, cost in graph[u]:
        if dist[vertex] is None or dist[u]+cost < dist[vertex]:
            dist[vertex] = dist[u] + cost
            heappush(heap, (dist[vertex], vertex)) 
    
print(maxPing-minPing)
