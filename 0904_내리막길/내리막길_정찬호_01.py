import sys
sys.setrecursionlimit(100000)


def dfs(cxy):
    cx, cy = cxy

    if cx == m-1 and cy == n-1:  # 경로 도착지에 도착?
        cnt_list[cx][cy] += 1    # cnt_list의 도착지 값 1로 설정 
        return True

    for dx, dy in dxy:           # 4방향 확인 
        nx, ny = cx + dx, cy + dy

        if nx < 0 or ny < 0 or nx >= m or ny >= n: continue
        if maps[cx][cy] <= maps[nx][ny]: continue  # 경로 따라서
        if cnt_list[nx][ny] == -1: continue        # 연결된 곳 없으면 다음 경로 확인
        if cnt_list[nx][ny] != 0:                  # 연결된곳 있으면 
            cnt_list[cx][cy] += cnt_list[nx][ny]   # 4방향중 끝과 연결된 경로 갯수만큼 + 
            continue
            
        # 다음 갈곳이 있긴 하지만, 해당 부분이 0 ( 들른적이 없으면 ) dfs 진행 
        tf = dfs((nx, ny))
        if tf:  cnt_list[cx][cy] += cnt_list[nx][ny] 
            # tf True : 도착점과 연결되어 있으므로, 해당 값만큼 + 

    if cnt_list[cx][cy] != 0:        return True  # 4방향중 연결된 곳 있다면 True 반환 
    else:
        # if cx == 0 and cy == 0:  # 시작 지점까지 끌고왔는데 0이다? 연결된 경로가 없다. 
        #     cnt_list[0][0] = 0
        #     return
        
        # 시작 지점 아닌데 4방향 봤는데도 0 -> 연결된 곳 없다 -> -1로 설정
        cnt_list[cx][cy] = -1   
        return False


dxy = [(1,0), (0,1), (-1,0), (0,-1)]
m, n = map(int, input().split())  # m 행 / n 열
maps = [list(map(int, input().split())) for _ in range(m)]
cnt_list = [[0] * n for _ in range(m)]  # 초기값 0 

dfs((0, 0))
print(cnt_list)
print(cnt_list[0][0])

