from collections import deque


def bfs():
    visited = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((0,0))

    visited[0][0] = 0  # 첫방은 무조건 흰방 => 방 안바꿔도 되므로


    while queue:
        cx, cy = queue.popleft()

        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = dx+cx, dy+cy

            if nx < 0 or ny < 0 or nx >= n or ny >= n:continue

            flag = 0

            if maps[nx][ny] == 0:  # 검은방
                # 방문 한번도 안했으면 내가 온 방향 카운터 +
                if visited[nx][ny] == -1:  
                    visited[nx][ny] = visited[cx][cy] + 1
                    flag = 1
                else:  # 방문 했었으며 내가 끌고 온것과 비교  >  # 내가 끌고온게 최소야 > 값 바꿔줘야
                    if visited[cx][cy] + 1 < visited[nx][ny]: 
                        visited[nx][ny] = visited[cx][cy] + 1
                        flag = 1

            else:  # 흰방
                if visited[nx][ny] == -1:  
                    visited[nx][ny] = visited[cx][cy]  # 방문 안했었으면 가져온 값 그대로 넣기
                    flag = 1
                else:  # 방문 했었으면 내가 끌고 온것과 비교
                    if visited[cx][cy] < visited[nx][ny]:
                        visited[nx][ny] = visited[cx][cy]
                        flag = 1
    
            if flag == 1:
                queue.append((nx, ny))

    return visited[n-1][n-1]


n = int(input())
maps = [list(map(int, input())) for _ in range(n)]
print(bfs())