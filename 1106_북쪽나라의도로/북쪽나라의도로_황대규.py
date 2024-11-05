# 조건에서 모든 도시는 다른 모든 도시로 이동할 수 있다고 했다
# 하나의 점에서 가장 멀리갈 수 있는 도시를 찾는다.
# 그 점을 출발지로 다시 가장 멀리갈 수 있는 도시를 찾는다
# 그 길이가 정답

from collections import deque

def bfs(x):
    visit[x] = 0
    q = deque([x])
    while q:
        x = q.popleft()
        for i, w in arr[x]:
            if visit[i] == -1:
                visit[i] = visit[x] + w
                q.append(i)

arr = [[] for _ in range(10002)]

while True:
    try:
        a, b, w = map(int, input().split())
        arr[a].append((b, w))
        arr[b].append((a, w))
    except:
        break

visit = [-1 for _ in range(10002)]
bfs(1)
s = visit.index(max(visit))
visit = [-1 for _ in range(10002)]
bfs(s)
print(max(visit))