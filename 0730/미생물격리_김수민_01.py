T = int(input())
 
for test_case in range(1,T+1):
    arr_size,hour,mis=map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(mis)]
    hap = 0
    dxy = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]
    while hour > 0:
        for j in range(mis):
            # 이동
            dir = arr[j][3]
            if dir == 0: continue
            arr[j][0] += dxy[dir][0]
            arr[j][1] += dxy[dir][1]
            if arr[j][1]==0 or arr[j][0]==0 : #좌/상
                arr[j][3] += 1 #방향 바꾸기
                arr[j][2] = arr[j][2]//2
            elif arr[j][1]==arr_size-1 or arr[j][0]==arr_size-1 : #우/하
                arr[j][3] -= 1
                arr[j][2] = arr[j][2]//2

            # if arr[j][3]==1 : #상
            #     arr[j][0]-=1
            # elif arr[j][3]==2 : #하
            #     arr[j][0]+=1
            # elif arr[j][3]==3 : #좌
            #     arr[j][1]-=1
            # elif arr[j][3]==4 : #우
            #     arr[j][1]+=1
         
        # 정렬 (x,y) 정렬하고, 미생물 수는 내림차순으로 정렬
        arr = sorted(arr, key=lambda x: (x[0], x[1],-x[2]))

        # 위로 올렸음
        # for j in range(mis): # 약품에 닿을 때
        #     if arr[j][1]==0 or arr[j][0]==0 : #좌/상
        #         arr[j][3] += 1 #방향 바꾸기
        #         arr[j][2] = arr[j][2]//2
        #     elif arr[j][1]==arr_size-1 or arr[j][0]==arr_size-1 : #우/하
        #         arr[j][3] -= 1
        #         arr[j][2] = arr[j][2]//2

        # len(arr)-1 대신 mis
        for j in range(mis-1):
            # 군집 모이는 경우
            if arr[j][0] == -1: continue
            if arr[j][0]==arr[j+1][0] and arr[j][1]==arr[j+1][1] :
                arr[j+1][3]=arr[j][3] # 이동 방향 흡수
                arr[j+1][2]+=arr[j][2] # 미생물 수 더하기
 
                # 흡수할 거 했으니까 arr[j] 무력화시키기~.~
                arr[j] = [-1,-1,0,0]
                # arr[j][0]= -1
                # arr[j][1]=-1
                # arr[j][2]=0
                # arr[j][3]=0
 
        hour -=1
 
    for j in range(len(arr)): #살아남은 미생물 수만 더하기
        hap += arr[j][2]
 
    print(f'#{test_case} {hap}')