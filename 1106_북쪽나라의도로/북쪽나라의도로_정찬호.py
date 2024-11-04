import sys


def dfs(cur, depth, visited):
    global ans

    # 현재 노드 cur에서 이어진 모든 노드 v에 대해 탐색
    for v in graph[cur]:
        if v[0] in visited:  # 이미 방문한 노드라면 건너뜀
            continue
        visited.add(v[0])  # 노드 v[0]을 방문 목록에 추가

        # 깊이(거리)를 증가시키면서 DFS 재귀 호출
        dfs(v[0], depth + v[1], visited)
        visited.discard(v[0])  # DFS가 끝난 후 노드 v[0]을 방문 목록에서 제거

    # 최댓값 업데이트
    ans = max(ans, depth)
    return


# 입력 형식: 도시1, 도시2, 도로 길이(양방향 통행 가능) / 가장 먼 두 도시 사이의 거리를 출력하는 것이 목표
edges = []
while True:
    try:
        line = input().strip()
        if not line:
            continue  # 빈 줄이 입력된 경우 무시하고 다음 입력 대기
        edges.append(list(map(int, line.split())))  # 입력을 숫자로 변환하여 edges 리스트에 추가

    except EOFError:
        break  # EOFError 발생 시 입력 종료

if not edges:
    # 입력된 연결 도로가 없는 경우 결과는 0
    print(0)
else:
    # 그래프 생성 (양방향)
    graph = {}
    for edge in edges:  # edge = [도시1, 도시2, 도로 길이]
        a, b, w = edge
        # 도시 a에서 b로 가는 길이 w를 추가
        if a in graph:
            graph[a].append((b, w))
        else:
            graph[a] = [(b, w)]

        # 도시 b에서 a로 가는 길이 w를 추가 (양방향)
        if b in graph:
            graph[b].append((a, w))
        else:
            graph[b] = [(a, w)]

    ans = 0
    # 그래프의 각 노드에서 DFS 시작
    for node in graph:
        dfs(node, 0, {node})  # 시작 노드 node, 초기 거리 0, 방문한 노드 {node}

    # 가장 먼 거리 출력
    print(ans)
