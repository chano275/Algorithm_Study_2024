# b = list(zip(*a))[0] 0 번째 열 값들 가져옴
# n^2이지만 탐색 값이 2000 이하 가능

'''
열 연산은 전치행렬(행처리)로 돌린 후 계산하고 복구

숫자 카운트 안 좋았던 생각:
 오랜만에 c++을 봤어서 count를 할 때 배열을 100까지 미리 선언하고 거기에 숫자들을 올리자!라고 생각했었다.
개선:
 dict를 써서 get을 했을 때 값이 없으면 선언해주고, 값이 있으면 하나 올린 값 저장
'''

r, c, k = map(int, input().split())
r -= 1
c -= 1
arr = [list(map(int, input().split())) for _ in range(3)]

for ans in range(101):  # 100초 이내에 답 찾는 경우 break
    if arr[r][c]==k:
        break

    # 열연산인경우 전치행렬로 변환 원상복구
    do_col_cul = False
    if len(arr)<len(arr[0]):    # 열연산
        do_col_cul = True
        arr = list(map(list,zip(*arr)))

    # 행단위연산: 숫자와 카운트를 처리 => 정렬
    mxcol = 0
    for i in range(len(arr)):
        cnts = {}
        for j in range(len(arr[i])):
            if arr[i][j]==0:    
                continue    # 0이라면 카운트하지 않음
            if arr[i][j] in cnts:           # 이미 있는 숫자면 +1
                cnts[arr[i][j]]+=1
            else:                           # 없는 숫자면 1개!
                cnts[arr[i][j]]=1

        # 1. 수의 등장 횟수가 커지는 순으로
        # 2. 수가 커지는 순으로 정렬
        lsts = sorted(cnts.items(), key=lambda x:(x[1],x[0])) 

        arr[i] = [n for lst in lsts for n in lst]
        mxcol = max(mxcol, len(arr[i]))

    # 최대길이(mxcol) 구해서 자르거나 0으로 채우기
    mxcol = min(mxcol, 100)
    for i in range(len(arr)):
        while len(arr[i])<mxcol:    # 0으로 채워야함
            arr[i].append(0)
        while len(arr[i])>mxcol:    # 뒤부터 지워야함
            arr[i].pop()

    if not do_col_cul:                # 원상복구
        arr = list(map(list,zip(*arr)))
else:                   # 100초까지 답을 못찾은 경우 -1출력
    ans = -1
print(ans)
