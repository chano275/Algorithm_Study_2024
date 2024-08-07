T = int(input())


def check_load(line):
    # 연속된 숫자의 갯수
    cnt = 1
    for i in range(N - 1):
        # 지금 타일과 다음 타일의 높이가 같은경우
        if line[i] == line[i + 1]:
            cnt += 1
        # 지금 타일보다 다음 타일이 1 높은 경우 and 낮은 타일이 x이상일 경우
        elif line[i + 1] - line[i] == 1 and cnt >= X:
            cnt = 1
        # 지금 타일보다 다음 타일이 1 낮은 경우 and 경사로 다음 바로 경사로 인지 확인
        elif line[i] - line[i + 1] == 1 and cnt >= 0:
            # 경사로의 X의 길이 이상인것을 체크용
            # 0이 아닌 -X 하는 이유? -> 3322233 처럼 양쪽에 경사로가 필요한 경우를 고려
            cnt = -X + 1
        # 높이가 2이상 차이날 경우 or 경사로 길이가 부족한 경우 or 양쪽에 경사로가 필요하지만 부족한 경우 등등
        else:
            return 0
    if cnt >= 0:
        return 1
    else:
        return 0


for test_case in range(1, T + 1):
    N, X = map(int, input().split())
    ans = 0
    # 기본적인 지면 정보 저장
    ground = [list(map(int, input().split())) for _ in range(N)]
    # 시계방향으로 90도 회전 하기 위한 배열
    rotate_ground = [[-1] * N for _ in range(N)]
    # 반복문을돌며 한줄씩 check_load 함수를 통해 가로 활주로 확인
    for i in range(N):
        ans += check_load(ground[i])
        for j in range(N):
            # 2차원 배열 90도 회전
            rotate_ground[i][j] = ground[N - j - 1][i]
    # 회전한 배열을 통해 세로 활주로 체크
    for line in rotate_ground:
        ans += check_load(line)

    print(f'#{test_case} {ans}')