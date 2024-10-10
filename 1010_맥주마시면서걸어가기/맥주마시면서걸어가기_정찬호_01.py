from collections import deque  # deque를 사용하기 위해 collections 모듈에서 deque를 가져옴

tc = int(input())  # 테스트 케이스 수 입력

for _ in range(tc):
    n = int(input())  # 편의점의 수 입력
    home_x, home_y = map(int, input().split())  # 집의 x, y 좌표 입력
    conv = [list(map(int, input().split())) for _ in range(n)]  # 각 편의점의 좌표 입력 (n개)
    pent_x, pent_y = map(int, input().split())  # 펜타포트 록 페스티벌 장소의 좌표 입력

    visited = set()  # 방문한 편의점 좌표를 저장할 집합
    flag = 0  # 목적지에 도달했는지 여부를 확인하는 플래그

    queue = deque()  # BFS를 위한 큐 생성
    queue.append((home_x, home_y))  # 처음에는 집에서 출발

    while queue:
        cx, cy = queue.popleft()  # 큐에서 현재 위치를 꺼냄
        if abs(cx - pent_x) + abs(cy - pent_y) <= 1000:  # 현재 위치에서 목적지까지 1000m 이내면
            print('happy')  # 도달 가능하므로 'happy' 출력
            flag = 1  # 플래그 설정
            break  # 탐색 종료

        for dx, dy in conv:  # 모든 편의점 좌표에 대해 탐색
            if (dx, dy) in visited: continue  # 이미 방문한 편의점이면 건너뜀

            # 현재 위치에서 편의점까지 1000m 이내면
            if abs(dx - cx) + abs(dy - cy) <= 1000:
                queue.append((dx, dy))  # 그 편의점 좌표를 큐에 추가
                visited.add((dx, dy))  # 방문한 편의점으로 추가

    if flag == 1:  # 목적지에 도달했으면
        continue  # 다음 테스트 케이스로 넘어감
    else:
        print('sad')  # 목적지에 도달하지 못했으면 'sad' 출력
