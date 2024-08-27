import heapq
r, c, k = list(map(int, input().split()))
maps = [list(map(int, input().split())) for _ in range(3)]
a = [p[:] for p in maps]

time, ans = 0, -1

for _ in range(101):

    # 탈출조건 체크.
    # r, c에 k값이 있는지 확인할 때에 index 밖에 r, c가 있는 경우 존재.
    # 그런 경우들은 탈출조건 확인하지 않고 pass 하여 연산 짆애
    if r-1 > len(a)-1 or c-1 > len(a[0])-1:
        pass
    else:
        if a[r-1][c-1] == k:
            # 들어오자마자 답인 경우가 있으므로, 연산 이전에 미리 배열을 check
            # 탈출조건 만족하면 걸린 시간 return하며 반복문 중단
            ans = time
            break

    # 탈출하지 않으면 미리 시간 +
    time += 1

    # 가로 세로를 비교해 연산 진행해야 하므로 저장해놓고
    # zero padding 할 때에 사용할 변수 max_length 선언해놓음
    g, s, max_length = len(a[0]), len(a), 0  # 열 행

    temp = []
    if s >= g:  # 배열 그대로 확인 ( 가로 정렬 시 )

        # 각 줄에 대한 정렬 진행
        for line in a:
            heap_temp, heap, b = [], [], [0] * (max(line) + 1)
            # b : 각 숫자가 몇번 나왔는지 check ( 가중치 )  /  0번 idx 사용하지 않음

            for num in line:
                b[num] += 1  # 가중치 check ( 몇개 나왔는지 )

            for i in range(1, len(b)):  # b를 돌며
                if b[i] == 0: continue  # 하나도 안나온건 무시하고
                heapq.heappush(heap, (b[i], i))  # 나온게 숫자라면 가중치, 해당 숫자를 hq에 저장

            while heap:  # heap 돌면서 가중치 / 숫자 크기 순으로 heap pop 해주고
                a = (heapq.heappop(heap))

                # heap_temp 배열에 해당 숫자 / 나온 갯수 ( 가중치 ) 적어줌
                heap_temp.append(a[1])
                heap_temp.append(a[0])

            # 한 line에 대한 정렬 끝났으므로, temp에 붙여주고
            temp.append(heap_temp)
            # zero padding 할 때에 쓸 max_length update
            max_length = max(max_length, len(heap_temp))

        # max_length 만큼의 길이가 안되는 리스트들에 zero padding
        a = []
        for zero_padding in temp:
            if len(zero_padding) != max_length:
                for _ in range(abs(len(zero_padding) - max_length)):
                    zero_padding.append(0)
            a.append(zero_padding)

    else:  # 세로 정렬 시

        # 배열 돌리기 -> 직사각형일 수 있으므로, 돌린 배열을 0으로 다 채워놨다고 가정하고, 값만 넣어줌
        s, g = len(a), len(a[0])
        temp = [[0] * s for _ in range(g)]
        for i in range(s):
            for j in range(g):
                temp[j][i] = a[i][j]
        a = temp

        # 위와 동일한 정렬 연산
        temp = []
        for line in a:
            heap_temp, heap = [], []
            b = [0] * (max(line) + 1)
            for num in line:  b[num] += 1
            for i in range(1, len(b)):
                if b[i] == 0: continue
                heapq.heappush(heap, (b[i], i))

            while heap:
                a = (heapq.heappop(heap))
                heap_temp.append(a[1])
                heap_temp.append(a[0])
            temp.append(heap_temp)
            max_length = max(max_length, len(heap_temp))

        # 위와 동일한 zero padding
        a = []
        for zero_padding in temp:
            if len(zero_padding) != max_length:
                for _ in range(abs(len(zero_padding) - max_length)):
                    zero_padding.append(0)
            a.append(zero_padding)

        # 위와 동일한 돌리기
        s, g = len(a), len(a[0])
        temp = [[0] * s for _ in range(g)]
        for i in range(s):
            for j in range(g):
                temp[j][i] = a[i][j]
        a = temp

    # 연산 끝난 배열의 각 행 / 열이 100 넘어간다면 컷
    s, g = len(a), len(a[0])
    temp = []
    if s > 100 and g > 100:
        for i in range(100):
            for j in range(100):
                temp[i][j] = a[i][j]
                a = temp
    elif s > 100:
        for i in range(100):
            for j in range(g):
                temp[i][j] = a[i][j]
                a = temp
    elif g > 100:
        for i in range(s):
            for j in range(100):
                temp[i][j] = a[i][j]
                a = temp

print(f'{ans}')