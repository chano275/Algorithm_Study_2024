'''
문제에서 신경써야할 조건 정리
1. 미생물 군집이 arr 사이드에 닿으면 virus_count는 2로 나눈다, move_di의 방향은 반대로 바꿔준다
2. 미생물 수가 0이되는 집단은 사라진다
3. 이동 후 두 개 이상의 군집이 한 셀에 모이는 경우 군집들이 합쳐진다 => 생각 : 그렇다면 arr를 3중 배열을 사용해서??
메모리 오류 가능성이 너무 높다 그럼 dict를 던지자
4. 군집이 합쳐질 때 고려해야하는 것은 이동방향 이동방향은 virus_count가 가장 많은 군집의 이동방향으로

*** 핵심
x_pos, y_pos, virus_count, move_di
0      1      2           3


x, y, virus_num, virus_di는 for문 내에서 dict의 내용을 바꾸기 위해 사용하는 변수
'''

# 방향전환 알고리즘 생각한 방식
# 인덱스가 홀수인 경우 -1 인덱스가 짝수인 경우 +1하는 방식으로
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cell_count, time, virus_group_count = map(int, input().split())
    virus_info = {}
    answer = 0
    arr = [[-1] * cell_count for _ in range(cell_count)]

    # 입력 받는 구간
    for i in range(virus_group_count):
        x_pos, y_pos, virus_count, move_di = map(int, input().split())
        virus_info[i] = ([x_pos, y_pos, virus_count, move_di-1])
        arr[x_pos][y_pos] = i

    '''
    알고리즘 생각 예제
    for문을 돌리지 않고 한번에 처리하는 방식 생각 
    but 가로 축 이동 군집 세로축 이동 군집의 교차를 어떻게 처리해야할지 모르겠어서 pass
    결국 그냥 for문을 돌리는 시물레이션 문제로 구현할 예정
    ''' # 알고리즘 생각 과정

    # # 시물레이션 시작
    for hour in range(time):
        compare = []
        for num in range(virus_group_count):
            if virus_info[num]:
                x = virus_info[num][0]
                y = virus_info[num][1]

                nx = x + dx[virus_info[num][3]]
                ny = y + dy[virus_info[num][3]]

                virus_num = virus_info[num][2]
                virus_di = virus_info[num][3]
                if nx <= 0 or ny <= 0 or nx >= cell_count - 1 or ny >= cell_count - 1:  # 빨간 셀에 닿은 경우
                    virus_num = virus_num // 2
                    if virus_info[num][3] % 2 == 0:                   # 위에서 적은대로 인덱스가 짝수인 경우 +1
                        virus_di = virus_di + 1
                    else:
                        virus_di = virus_di - 1

                # 충돌
                if arr[nx][ny] == -1:                           # 비어있는 경우
                    arr[x][y] = -1                              # 원래 있던 곳 비우고
                    arr[nx][ny] = num                           # 새로운 곳 채워주기
                    virus_info[num] = ([nx, ny, virus_num, virus_di])
                else:                                          # 비어있지 않을 경우
                    compare_num = arr[nx][ny]
                    total_virus_num = virus_num + virus_info[compare_num][2]
                    arr[x][y] = -1
                    if virus_num <= virus_info[compare_num][2]:
                        virus_info[compare_num] = ([nx, ny, total_virus_num, virus_info[compare_num][3]])
                        virus_info[num] = None                  # 미생물 수 적은 아이 삭제
                    else:
                        virus_info[num] = ([nx, ny, total_virus_num, virus_di])
                        virus_info[compare_num] = None
                        arr[nx][ny] = num

    for num in range(virus_group_count):
        if virus_info[num]:
            answer += virus_info[num][2]

    print(f'#{test_case} {answer}')

