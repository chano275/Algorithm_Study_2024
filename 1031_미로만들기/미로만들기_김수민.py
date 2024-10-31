from collections import deque
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def miro(grid, n):
    costs = [[float('inf')] * n for _ in range(n)]
    costs[0][0] = 0  
    queue = deque([(0, 0, 0)]) 

    while queue:
        cost, x, y = queue.popleft()

        if x == n - 1 and y == n - 1:
            return cost

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost if grid[nx][ny] == 1 else cost + 1
                
                if new_cost < costs[nx][ny]:
                    costs[nx][ny] = new_cost
                    if grid[nx][ny] == 1:
                        queue.appendleft((new_cost,nx, ny))  # 비용이 동일할 때 앞에 추가
                    else:
                        queue.append((new_cost,nx, ny))  # 비용 증가 시 뒤에 추가

n = int(input())
grid = [list(map(int, input().strip())) for _ in range(n)]

min_cost = miro(grid, n)

print(min_cost)
