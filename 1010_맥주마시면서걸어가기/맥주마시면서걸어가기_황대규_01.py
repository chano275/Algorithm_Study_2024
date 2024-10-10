from collections import deque


def bfs(start, festival, stores, n):
    queue = deque([start])
    visited = [False] * (n + 2)
    visited[0] = True

    while queue:
        current_x, current_y = queue.popleft()

        # 현재 위치에서 페스티벌까지 갈 수 있는지 확인
        if abs(current_x - festival[0]) + abs(current_y - festival[1]) <= 1000:
            return "happy"

        # 편의점을 하나씩 확인
        for i in range(1, n + 2):
            if not visited[i]:
                store_x, store_y = stores[i]
                if abs(current_x - store_x) + abs(current_y - store_y) <= 1000:
                    visited[i] = True
                    queue.append((store_x, store_y))

    return "sad"


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())  # 편의점 개수
        stores = []

        # 집 좌표
        home_x, home_y = map(int, input().split())
        stores.append((home_x, home_y))

        # 편의점 좌표 입력
        for _ in range(n):
            store_x, store_y = map(int, input().split())
            stores.append((store_x, store_y))

        # 페스티벌 좌표
        fest_x, fest_y = map(int, input().split())
        stores.append((fest_x, fest_y))

        # BFS 탐색 시작
        result = bfs(stores[0], stores[-1], stores, n)
        print(result)


main()