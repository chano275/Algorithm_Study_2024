T = int(input())
for tc in range(1, T+1):
    n, x = map(int, input().split())
    flight = [list(map(int, input().split())) for _ in range(n)]

    def checker(line):
        cnt = 1 # 0번 idx를 찍고 시작 

        if len(line) < x : return 0

        for i in range(1, len(line)): 
            # 1번째 idx부터 맨 마지막까지 / 현재 보는 원소와 이전에 나왔던 원소를 비교한다 
            # range 에 대한 제약 줄이기

            # 현재 원소와 이전 원소의 비교 3가지 : + = - 

            if line[i] == line[i - 1]: # 동일하면 cnt 증가 ( 0, 1 idx가 동일하다면, cnt = 2)
                cnt += 1

            elif line[i] == line[i - 1] + 1: 
                # 하나 증가했다면 지금까지 지나온 길의 높이가 x만큼 동일했어야 한다
                if cnt >= x:     
                    # cnt가 x보다 크거나 같다면 ( x만큼 지나왔다면 ) 이상 없으므로 현재 보고 있는 +1된 원소의 cnt를 세기 시작 
                      cnt = 1
                else: 
                    # x만큼 지나오지 않았는데 상승? 문제가 있다
                    return 0

            elif line[i] == line[i - 1] - 1:
                # 하나 감소했다면, line[i]에서 시작해 x만큼이 line[i-1] -1 과 동일해야 한다.
                if cnt < 0: 
                    # 감소했을 때에 cnt가 - 라면 ( 바로 밑에 else문에서 줄어든 cnt를 갚기 전에 일이 터졌다면 )
                    return 0 # out
                else:
                    # 문제가 없었다면?
                    cnt = -x + 1
                    # 현재 보고있는 원소부터 시작하여 x개가 동일해야 하므로, 
                    # cnt = -x + 1로 설정하여 높이가 x만큼 동일함을 check

            else: # +-1 / 0 차이가 아니다 == 차이가 2 이상이다 ? 
                return 0 # out
        

        if cnt >= 0: # 다 끝난 이후에, cnt가 0 이상이라면 ( -1일때 생긴 빚을 다 값았거나 / 동일한 원소가 반복되고 있었다면 )
            return 1 # 문제 없다 
        else: # - 라면 ( 빚을 다 못 갚았는데 끝났다 ? )
            return 0 # out 



    ans = 0

    for i in range(n): 
        ans += checker(flight[i])
        ans += checker([q[i] for q in flight])
        # filght 2차원배열에서 q를 뽑으면, 한 레코드(행)이 q에 들어감
        # 해당 q에서 i번째 원소를 pick / q가 flight만의 행 개수만큼 돎으로, 
        # 세로줄을 가져온다. 

    print(f'#{tc} {ans}')
