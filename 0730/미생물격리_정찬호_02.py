import sys
sys.stdin = open('sample_input (1).txt')
T = int(input())
for test_case in range(1, T + 1):
    n, m, k = list(map(int, input().split()))
    square = []

    for _ in range(k):  # k_x, k_y, k_num, k_dir
        square.append(list(map(int, input().split())))

    while m != 0:
        m -= 1

        k_set = set()
        collision = {}
        pop_idx = []

        for square_row in range(len(square)):
            # dir 따라 좌표 이동 + 빨간줄

            if square[square_row][2] < 2: pop_idx.append(square_row)  # 미생물 소멸 생각

            # 소멸 x
            if square[square_row][3] == 1:  # 상
                square[square_row][0] -= 1
                if square[square_row][0] == 0:
                    square[square_row][2] //= 2
                    square[square_row][3] = 2

            elif square[square_row][3] == 2:  # 하
                square[square_row][0] += 1
                if square[square_row][0] == n-1:
                    square[square_row][2] //= 2
                    square[square_row][3] = 1

            elif square[square_row][3] == 3:  # 좌
                square[square_row][1] -= 1
                if square[square_row][1] == 0:
                    square[square_row][2] //= 2
                    square[square_row][3] = 4

            elif square[square_row][3] == 4:  # 우
                square[square_row][1] += 1
                if square[square_row][1] == n-1:
                    square[square_row][2] //= 2
                    square[square_row][3] = 3

        # 이동 끝! 충돌 생각
        for collision_row in range(len(square)):
            s_len = len(k_set)
            k_set.add((square[collision_row][0], square[collision_row][1]))
            if s_len != len(k_set): continue  # 충돌이 난게 없으면 skip

            pop_idx.append(collision_row) # 이것들은 나중에 안걸렸던 중복 요소에 더해주고 다 pop 할 것
            try:  # dict 처음 들어왔으면 except 로 간다
                if collision[str(square[collision_row][0]) + '_' + str(square[collision_row][1])][0] < square[collision_row][2]: # max_val / sum / max_dir
                    collision[str(square[collision_row][0]) + '_' + str(square[collision_row][1])][0] = square[collision_row][2]
                    collision[str(square[collision_row][0]) + '_' + str(square[collision_row][1])][2] = square[collision_row][3]
                collision[str(square[collision_row][0]) + '_' + str(square[collision_row][1])][1] += square[collision_row][2]

            except:
                collision[str(square[collision_row][0]) + '_' + str(square[collision_row][1])] = [square[collision_row][2],square[collision_row][2],square[collision_row][3], square[collision_row][0], square[collision_row][1]]

        # collision 돌면서 넣어야지
        coll_list = list(collision.values())
        for coll_row in range(len(coll_list)):
            for chk in range(len(square)):
                if square[chk][0] == coll_list[coll_row][3] and square[chk][1] == coll_list[coll_row][4]:  # xy 일치
                    square[chk][2] += coll_list[coll_row][1]  # sum
                    if square[chk][2] < coll_list[coll_row][0]:  # dir 바꿔야
                        square[chk][3] = coll_list[coll_row][2]

        pop_idx.sort()
        for bye in range(len(pop_idx)):
            square.pop(pop_idx[bye] - bye)

    ans = 0
    for su in square:
        ans += su[2]

    print(f'#{test_case} {ans}')