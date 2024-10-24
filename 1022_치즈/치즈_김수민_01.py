from collections import deque


def melt_cheese(grid, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    cheese_to_melt = []

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if grid[nx][ny] == 1:
                    cheese_to_melt.append((nx, ny))
                elif grid[nx][ny] == 0:
                    queue.append((nx, ny))

    # 치즈 녹이기
    for cx, cy in cheese_to_melt:
        grid[cx][cy] = 0

    return len(cheese_to_melt)  # 녹은 치즈의 개수


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
count_of_ones = sum(row.count(1) for row in grid)

time = 0
last_cheese_count = 0

while True:
    melted_count = melt_cheese(grid, n, m)

    last_cheese_count = melted_count
    time += 1

    count_of_ones -= melted_count
    if count_of_ones == 0:  # 더 이상 녹을 치즈가 없으면 종료
        print(time)  # 모든 치즈가 녹는 데 걸린 시간
        print(last_cheese_count)  # 마지막 남은 치즈의 개수
        exit()
