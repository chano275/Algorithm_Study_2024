# 미세먼지 확산 방향 정의 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 미세먼지
def spread_dust():
    new_dust = [[0] * M for _ in range(N)]  # 새로운 미세먼지 보드 초기화
    for r in range(N):
        for c in range(M):
            if board[r][c] > 0:  # 미세먼지가 있는 경우
                spread_amount = board[r][c] // 5  # 확산할 양 계산
                for dr, dc in directions:  # 4방향으로 확산
                    nr, nc = r + dr, c + dc
                    # 경계 및 공기청정기 확인
                    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != -1:
                        new_dust[nr][nc] += spread_amount  # 인접 셀에 미세먼지 추가
                        new_dust[r][c] -= spread_amount  # 현재 셀에서 미세먼지 감소\
    # 새로운 미세먼지 상태를 기존 보드에 업데이트
    for r in range(N):
        for c in range(M):
            board[r][c] += new_dust[r][c]

# 공기청정기
def operate_air_purifier():
    # 상단 공기청정기 작동 (시계방향)
    top_air=air_purifier[0]
    for i in range(top_air, -1, -1):
        if board[i][0] == -1: # 공기청정기 위치
            continue
        board[i][0] = board[i-1][0]  # 위에서 아래
    for j in range(M-1):
        board[0][j] = board[0][j+1]  # 오른쪽에서 왼쪽
    for i in range(top_air):
        board[i][M-1] = board[i+1][M-1]  # 아래서 위로
    for j in range(M-1, 0, -1):
        board[top_air][j] = board[top_air][j-1]  # 왼쪽에서 오른쪽
    board[top_air][1] = 0  # 공기청정기에서 나오는 부분은 0으로 설정

    # 하단 공기청정기 작동 (반시계방향)
    down_air=air_purifier[1]
    for i in range(down_air, N-1):
        if board[i][0] == -1: # 공기청정기 위치
            continue 
        board[i][0] = board[i+1][0]  # 아래에서 위
    for j in range(M-1):
        board[N-1][j] = board[N-1][j+1]  # 오른쪽에서 왼쪽
    for i in range(N-1, down_air, -1):
        board[i][M-1] = board[i-1][M-1]  # 위에서 아래
    for j in range(M-1, 0, -1):
        board[down_air][j] = board[down_air][j-1]  # 왼쪽에서 오른쪽
    board[down_air][1] = 0  # 공기청정기에서 나오는 부분은 0으로 설정


# def print_board():
#     for i in range(N):
#         for j in range(M):
#             print(board[i][j], end=' ')
#         print()

# 입력 처리
N, M, T = map(int, input().split())  # N: 행, M: 열, T: 시간
board = [list(map(int, input().split())) for _ in range(N)]  # 보드 초기화

# 공기청정기 위치 저장
air_purifier = []
for i in range(N):
    for j in range(M):
        if board[i][j] == -1:  # 공기청정기 위치 확인
            air_purifier.append(i)

# T초 동안 미세먼지 확산과 공기청정기 작동 반복
for _ in range(T):
    spread_dust()  # 미세먼지 확산
    # print_board()
    # print('미세먼지 확산 완료')
    operate_air_purifier()  # 공기청정기 작동
    # print_board()
    # print('공기청정기 작동')

# print('-----')
# print('최종 미세먼지')
# print_board()
# 최종적으로 남아 있는 미세먼지의 총합 계산
total_dust = sum(sum(cell for cell in row if cell > 0) for row in board)
print(total_dust)  # 결과 출력


'''191
8 8 2
3 0 0 0 0 0 0 0
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
'''
