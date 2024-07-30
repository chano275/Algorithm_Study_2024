dxy = {'1': [-1, 0],'2': [1, 0],'3': [0, -1],'4': [0, 1]} # dir의 값 1 ~ 4에 따라서 이동할 dx, dy를 제공


T = int(input())
for test_case in range(1, T + 1):
    k_dict = {}  # 미생물의 초기 자리에 대한 입력을 받을 dict를 선언
    n, m, k = list(map(int, input().split()))    # n : 구역의 한 변에 있는 셀의 개수 ( 가로 )    # m : 격리 시간    # k : 미생물 군집 개수
    for i in range(k):  # 맨 처음에 겹치는 좌표 가지는게 없으므로, 해당 행_열 이라는 키값에 현재 행 / 열 좌표, 값, dir 넣어줌
        k_i, k_j, k_num, k_dir = list(map(int, input().split()))
        k_dict[str(k_i) + '_' + str(k_j)] = [k_i, k_j, k_num, k_dir]

    # m 시간동안 dir 값을 확인해서 해당 방향으로 이동하고, 벽 / 충돌 일어나면 바꿔주기
    while m != 0:
        m -= 1

        dict_list = list(k_dict.values())  # 요소를 확인하고, 컨트롤하기 위해 list화\
        chk_set = set()  # 충돌 확인할 set
        temp_dict = {}

        for i in range(len(dict_list)):
            if dict_list[i][3] == -1:  # 이후 충돌이 난 경우에는 dir 값을 -1로 설정하여 확인하지 않고 건너가게 함
                continue
            loop_x, loop_y, loop_num, loop_dir = dict_list[i]

            ############################################################################
            # dir 에 따른 다음 좌표 nx, ny 설정하고, 저장
            nx, ny = loop_x + dxy[str(loop_dir)][0], loop_y + dxy[str(loop_dir)][1]
            dict_list[i][0], dict_list[i][1] = nx, ny
            ############################################################################

            ############################################################################
            # 빨간색 들어가는 경우의 값 / 방향 저장 및 dir 반대로
            if nx == n-1 or nx == 0 or ny == n-1 or ny == 0:
                if dict_list[i][2] < 2:
                    dict_list[i][3] = -1
                    continue
                dict_list[i][2] //= 2
                if loop_dir == 1:dict_list[i][3] = 2
                elif loop_dir == 2:dict_list[i][3] = 1
                elif loop_dir == 3:dict_list[i][3] = 4
                elif loop_dir == 4:dict_list[i][3] = 3

                continue # 빨간색이면 x, y, 값, dir 다 넘겼으므로 다음 요소 확인
            ############################################################################

            ############################################################################
            # 빨간색 들어가지 않는 정상적인 경우 - 충돌 생각
            set_len1 = len(chk_set)
            chk_set.add((nx, ny)) # 이동할 좌표가 벽이 아니니, 충돌하는지를 확인 위해 set의 len 으로 판단
            set_len2 = len(chk_set)

            # 정상적으로 추가된 요소 : num 과 dir 안바꿔도 되니깐 pass / 다음 x, y좌표는 위에서 이미 바꿨음
            if set_len1 != set_len2: pass

            else:  # 충돌 일어남 / 충돌된 요소의 dir을 -1로 바꾸어 확인을 건너뛰게 함
                dict_list[i][3] = -1

                if temp_dict.get(str(nx) + '_' + str(ny)) is None:
                    temp_dict[str(nx) + '_' + str(ny)] = [[dict_list[i][2]], [dict_list[i][3]]]

                    for j in range(0, i+1):  # i 까지 돌면서
                        if dict_list[j][0] == nx and dict_list[j][1] == ny:
                            dict_list[j][3] = -1
                            temp_dict[str(nx) + '_' + str(ny)][0].append(dict_list[j][2])
                            temp_dict[str(nx) + '_' + str(ny)][1].append(dict_list[j][3])

                # dict 에 있으면 비교 dict 값 바꾸기 // 여러개가 쌓일 수 있으니까 밑에서 for 또 돌면서 while 넘어가기 전에 세팅 후 초기화
                else:  # 있던 요소면
                    temp_dict[str(nx) + '_' + str(ny)][0].append(dict_list[i][2])
                    temp_dict[str(nx) + '_' + str(ny)][1].append(dict_list[i][3])

        temp_list = list(temp_dict.items())
        for p in range(len(temp_dict)):
            k_i, k_j = temp_list[p][0].split('_')
            k_num = sum(temp_list[p][1][0])
            k_dir = temp_list[p][1][1][temp_list[p][1][0].index(max(temp_list[p][1][0]))]
            k_dict[(k_i) + '|' * m + (k_j)] = [int(k_i), int(k_j), k_num, k_dir]

    ans = 0
    dict_list = list(k_dict.values())
    for i in range(len(dict_list)):        ans += dict_list[i][2]

    print(f'#{test_case} {ans}')

