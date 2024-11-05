# https://www.acmicpc.net/problem/1595
import sys

sys.stdin = open('input_1595.txt','r')


# 깊이 우선 탐색(DFS)을 이용해 트리에서 가장 먼 노드를 찾는 함수
def DFS(node, length):
    global ans  # 가장 긴 거리 저장
    global node_idx  # 최대 거리의 끝 노드 저장
    visited.add(node)  # 현재 노드를 방문했다고 표시

    # 현재 노드에서 인접한 노드를 탐색
    for [next_node, edge] in graph[node]:
        if next_node not in visited:  # 아직 방문하지 않은 노드라면
            ans = max(ans, length + edge)  # 최대 거리를 갱신
            if ans == length + edge:  # 최대 거리가 갱신되면 노드도 업데이트
                node_idx = next_node
            DFS(next_node, length + edge)  # DFS 재귀 호출


graph = {}  # 트리의 그래프를 저장할 딕셔너리

# 입력 받기 (트리의 간선 정보)
while True:
    try:
        a, b, c = map(int, input().split())  # a, b는 노드, c는 간선의 길이
        if a not in graph:  # a 노드가 없으면 추가
            graph[a] = []
        if b not in graph:  # b 노드가 없으면 추가
            graph[b] = []

        # 양방향 그래프 구축
        graph[a].append([b, c])
        graph[b].append([a, c])
    except:
        if not graph:  # 그래프가 비어있으면 입력이 잘못된 것
            print(0)
            exit()
        break  # 입력이 끝났을 때 종료

ans = 0  # 최대 거리 초기화
node_idx = 0  # 가장 긴 거리의 끝 점 초기화
visited = set()  # 방문한 노드들을 저장할 집합

# 임의의 시작점 (1번 노드)에서 DFS 시작
DFS(1, 0)

ans = 0  # 최대 거리 초기화 (다시 사용)
visited.clear()  # 방문 기록 초기화

# DFS가 끝난 후 가장 먼 노드를 찾았으면, 그 노드에서 다시 DFS를 수행
DFS(node_idx, 0)

# 결과 출력
print(ans)
