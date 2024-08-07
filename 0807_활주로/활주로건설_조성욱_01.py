T = int(input())

for test_case in range(1, T + 1):
    size, slope = map(int, input().split())
    runway_map = [list(map(int, input().split())) for _ in range(size)]
    tp_map = [[0]*size for _ in range(size)]
    build = False
    count = 0


    def line_check(array):
        construction = [[0] * size for _ in range(size)]  # 건설된 위치릂 표시하는 배열
        global count
        for i in range(size):
            for j in range(size-1):
                head, tail = array[i][j], array[i][j+1]  # 인접한 두 칸을 탐색 (head, tail)
                if abs(head-tail) > 1:  # head와 tail간 차이의 절댓값이 1 초과일 경우 다음 줄로 넘어감
                    build = False
                    break
                elif abs(head-tail) == 0:  # 차이가 0일 경우 다음 칸으로 진행
                    build = True
                    continue
                else:  # head와 tail간 차이의 절댓값이 1일 경우
                    if head > tail:  # 앞이 더 큰 경우 3222같은 경우
                        if j+slope > size-1:  # 경사로가 배열의 범위를 넘어가면 설치 불가, 다음 줄로 넘어감
                            build = False
                            break
                        for k in range(slope):  # 경사로가 지어져야 할 부분에 이미 경사로가 있는지, 경사로가 평평한지 판단
                            if construction[i][j+1+k] == 1 or array[i][j+1+k] != tail:
                                build = False
                                continue
                            construction[i][j+1+k] = 1
                            build = True  # 지어질 수 있을 경우 build에 True할당
                        if build == False:  # 지어질 수 없을 경우 다음 줄로 넘어감
                            break
                    else:  # 뒤가 더 큰 경우 2223 같은 경우
                        if j-slope+1 < 0:  # 경사로가 배열의 범위를 넘어가면 설치 불가, 다음 줄로 넘어감
                            build = False
                            break
                        for k in range(slope):  # 경사로가 지어져야 할 부분에 이미 경사로가 있는지, 경사로가 평평한지 판단
                            if construction[i][j-k] == 1 or array[i][j-k] != head:
                                build = False
                                continue
                            construction[i][j-k] = 1
                            build = True  # 지어질 수 있을 경우 build에 True할당
                        if build == False:  # 지어질 수 없을 경우 다음 줄로 넘어감
                            break
            if build == True:  # build가 True이면 활주로를 건설 가능한 줄
                count += 1


    def transpose(array, tp_array):  # 전치
        for i in range(size):
            for j in range(size):
                tp_array[i][j] = array[j][i]


    transpose(runway_map, tp_map)
    line_check(runway_map)
    line_check(tp_map)
    print(f'#{test_case} {count}')