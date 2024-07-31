T = int(input())
for tc in range(1, T+1):
    n,m,k = list(map(int, input().split()))
    micro_input = [list(map(int , input().split())) for _ in range(k)]

    back = {}
    forward = {}

    # 1 2 3 4 상 하 좌 우
    dxy = [(-1,0), (1,0), (0,-1), (0,1)]

    for micro in micro_input:
        back[(micro[0], micro[1])] = [(micro[2], micro[3])]

    for _ in range(m): # m 시간 동안 반복 > 끝나고 살아남은 미생물 총합 구하기
        forward = {}

        # x, y dir 확인하고 이동시켜야지
        for k, v in back.items():
            cx, cy = k
            num, dire = v[0]
            if dire == 1:cx -= 1 # 상 > cy num dire 그대로
            elif dire == 2: cx += 1
            elif dire == 3: cy -= 1
            else: cy += 1

            if cx == 0 or cx == n-1 or cy == 0 or cy == n-1:
                num //= 2
                if dire == 1: dire = 2
                elif dire == 2: dire = 1
                elif dire == 3: dire = 4
                elif dire == 4: dire = 3

            if num > 0:
                if (cx, cy) not in forward: #
                    forward[(cx, cy)] = [(num, dire)]
                else:
                    forward[(cx, cy)].append((num, dire))

        back = {}

        for k, v in forward.items():
            if len(v) >= 2:
                sum_num, max_num, max_dire = 0, 0, 0
                for (num_v, dire_v) in v:
                    if num_v > max_num:
                        max_num = num_v
                        max_dire = dire_v
                    sum_num += num_v
                back[k] = [(sum_num, max_dire)]
            else:
                back[k] = v

    ans = 0
    for ans_z in back:
        ans += back[ans_z][0][0]

    print(f'#{tc} {ans}')


