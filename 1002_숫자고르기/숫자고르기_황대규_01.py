'''
문제의 이해
첫 번째 시도 첫 줄과 둘째 줄 조합 중 최대값을 구하여라! => 문제 잘못 이해
두 번째 시도 dict를 활용해서 방문한 곳 저장 및 양방향 저장 진행 => 실패
세 번째 시도 dfs를 통해서 사이클을 찾아 사이클이 될 경우 result에 넣어준다
'''

n = int(input())
arr = [0] * (n + 1)
for i in range(1, n + 1):
    arr[i] = int(input())

result = []


def dfs(start):
    stack = []
    visited = [False] * (n + 1)  # 이번 DFS 중 방문 여부 확인
    current = start

    while not visited[current]:
        visited[current] = True
        stack.append(current)
        current = arr[current]

    if current == start:
        result.extend(stack)  # 사이클을 발견한 경우


for i in range(1, n + 1):
    dfs(i)

result = list(set(sorted(result)))
print(len(result))
for x in result:
    print(x)
