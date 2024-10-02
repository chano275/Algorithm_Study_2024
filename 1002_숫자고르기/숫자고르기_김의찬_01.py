import sys
# 표준 입력을 파일로부터 읽도록 설정
sys.stdin = open('input_2668.txt', 'r')

def DFS(store_start, start, visited):
    global ans  # 전역 변수 ans를 사용하여 사이클에 포함된 노드 저장
    # 시작 노드와 현재 노드가 같으면 사이클을 발견한 것
    if store_start == start:
        ans.update(visited)  # 방문한 모든 노드를 결과 집합에 추가
        return
    # 이미 방문한 노드라면 종료
    if start in visited:
        return
    visited.add(start)  # 현재 노드를 방문 리스트에 추가
    # 다음 노드로 DFS 호출
    DFS(store_start, num[start], visited)

# 입력 받기
N = int(input())  # 노드의 수
num = [0] + [int(input()) for _ in range(N)]  # 각 노드가 가리키는 노드 번호를 저장, 1-indexed

ans = set()  # 사이클에 포함된 노드 집합
visited = [False] * (N + 1)  # 방문한 노드 체크 리스트

# 각 노드에 대해 DFS 수행
for now in range(1, N + 1):
    temp_set = set()  # 현재 DFS에 사용될 방문 집합
    # 이미 사이클에 포함된 노드면 건너뛰기
    if now in ans:
        continue
    temp_set.add(now)  # 현재 노드 추가
    DFS(now, num[now], temp_set)  # DFS 시작
    visited[now] = True  # 현재 노드 방문 표시

# 결과 출력
print(len(ans))  # 사이클에 포함된 노드의 수 출력
list_ans = list(ans)  # 집합을 리스트로 변환
list_ans.sort()  # 정렬
for i in list_ans:  # 결과 출력
    print(i)
