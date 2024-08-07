def transpose(matrix): #전치행렬
    transposed = []
    for i in range(arr_size):
        new_row = [matrix[j][i] for j in range(arr_size)]
        transposed.append(new_row)
    return transposed

def check_height(current_row): # 행에서 같은 숫자가 몇 개 이상 연속되어 있는지, 연속된 숫자 길이의 최댓값 반환
    c_len=1
    m_len=1
    for j in range(0,arr_size-1):
        if arr[current_row][j]== arr[current_row][j+1]:
            c_len+=1
        else :
            m_len=max(c_len,m_len)
            c_len=1
    m_len=max(c_len,m_len)
    return m_len

def check_bridge():
    result=0
    for i in range(0,arr_size):
            bridgeable=check_height(i)
            if bridgeable == arr_size : # 평탄함
                result+=1
            elif bridgeable >= bridge : # 다리 놓을 수 있음
                duplicate_arr=[float(element) for element in arr[i]]
                check_arr=[True]*arr_size # 다리 끝 부분 놓을 수 있는지 확인

                j=0
                while j<arr_size-1 :
                    # 오른쪽에 다리 놓기 / 다리 오른쪽 끝이 배열 사이즈보다 작아야하고 / 다리 놓는 곳은 길이 같아야 함 / 다리 끝에 놓인게 없다
                    if duplicate_arr[j] - duplicate_arr[j+1] == 1 and j+bridge < arr_size and duplicate_arr[j+1]==duplicate_arr[j+bridge] and check_arr[j+bridge]==True:
                        for k in range(j+1,j+bridge): #다리 끝 부분 제외하고 0.5씩 더해서 경사 1 미만으로 줄임
                            duplicate_arr[k] += 0.5
                        check_arr[j+bridge]=False # 다리 끝 부분 겹치지 못하게 false로 재할당
                        j+=bridge-1
                    # 왼쪽에 다리 놓기 / 다리 왼쪽 끝이 배열 시작보다는 크거나 같아야하고 / 다리 놓는 곳은 길이가 같아야 함 / 다리 끝에 놓인게 없음
                    elif duplicate_arr[j] - duplicate_arr[j+1] == -1 and j-bridge+1 >= 0 and duplicate_arr[j]==duplicate_arr[j-bridge+1] and check_arr[j-bridge+1]==True:
                        for k in range(j,j-bridge+1,-1): #다리 끝 부분 제외하고 0.5씩 더해서 경사 1 미만으로 줄임
                            duplicate_arr[k] += 0.5
                        # check_arr[j-bridge+1]=False
                        # 어차피 오른쪽으로 계속 갈건데 얘는 false 처리 해봤자 이거 확인 안함
                    j+=1

                isbridge=True
                for j in range(0,arr_size-1) :
                    if abs(duplicate_arr[j]-duplicate_arr[j+1]) >= 1: # 1이상 차이나면 다리 설치해도 차이가 나니까 활주로 건설 불가 판정
                        isbridge=False
                        break
                     
                if isbridge : # 활주로 건설 되면
                    result+=1
    return result

T=int(input())
  
for tc in range(1,T+1) :
    arr_size, bridge=map(int,input().split())
    arr=[list(map(int, input().split())) for _ in range(arr_size)]
    result=0
  
    result += check_bridge()
    arr=transpose(arr)
    result += check_bridge()
      
    print(f'#{tc} {result}')