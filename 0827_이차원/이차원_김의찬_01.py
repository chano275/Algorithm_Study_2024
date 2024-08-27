# https://www.acmicpc.net/problem/17140
import sys
from queue import PriorityQueue
import heapq
sys.stdin = open('input_17140.txt','r')

T = 7
# PriorityQueue를 이욯하여 만든 함수 -> 백준은 PriorityQueue가 안됨 열받네?
def sort_r_use_PriorityQueue(arr_temp):
    # 옆으로 늘어날테니 늘어날 최대 값을 저장할 weight
    weight = 0
    # 바뀐? 배열들을 저장할 temp
    change_arr = []
    # 한줄씩 읽으며 숫자를 세고 배열을 바꿔줄 거임
    for line in arr_temp:
        # key : 숫자 , value : 횟수
        count = {}
        p_que = PriorityQueue()
        # 한줄씩 받아온것중 한칸씩 받으며 숫자의 카운트를 세어 count 딕셔너리에 저장
        for square in line:
            if square == 0 : continue
            if square in count: count[square] += 1
            else: count[square] = 1
        # 앞에서 찾은 숫자와 횟수를 우선순위큐를 활용하여 횟수 적은 순으로 정렬
        for key in count:
            p_que.put((count[key],key))
        # 바뀐 한줄을 저장할 배열
        change_line = []
        # 우선순위큐가 빌때까지 반복
        while not p_que.empty():
            # 우선순위 큐를 통해 횟수 적은순으로 정렬 되었기에 바로 저장해줌
            p_que_get = p_que.get()
            change_line += [p_que_get[1],p_que_get[0]]
        # 100개가 넘어갈 경우 잘라줌
        if len(change_line) > 100:
            change_line = change_line[:100]
        # 바뀐 한줄을 저장
        change_arr.append(change_line)
        # 최대 가로 길이를 구함
        weight = max(weight,len(change_line))
    # 최대 세로 길이를 구함
    height = len(change_arr)
    # 빈공간을 0으로 채우기 위해 우선 최대 사이즈로 0으로 구성된 2차원 배열 생성
    zero_base = [[0]*weight for _ in range(height)]
    # 0이아닌 값들 저장해줌
    for i in range(height):
        for j,v in enumerate(change_arr[i]):
            zero_base[i][j] = v

    return zero_base

# 백준을 위해 PriorityQueue 대신 heapq를 사용하여 대체
def sort_r_use_heapq(arr_temp):
    weight = 0
    change_arr = []
    for line in arr_temp:
        count = {}
        p_que = []
        for square in line:
            if square == 0 : continue
            if square in count: count[square] += 1
            else: count[square] = 1
        for key in count:
            heapq.heappush(p_que,(count[key],key))
        # print(p_que)
        change_line = []
        while p_que:
            p_que_get = heapq.heappop(p_que)
            change_line += [p_que_get[1],p_que_get[0]]
        if len(change_line) > 100:
            change_line = change_line[:100]
        change_arr.append(change_line)
        weight = max(weight,len(change_line))
    height = len(change_arr)
    zero_base = [[0]*weight for _ in range(height)]
    for i in range(height):
        for j,v in enumerate(change_arr[i]):
            zero_base[i][j] = v

    return zero_base

# 배열을 반시계방향으로 90도 회전하는 함수
def rotate_rever_clock(arr):
    height = len(arr)
    weight = len(arr[0])
    rotate_arr = [[0] * height for _ in range(weight)]
    for i in range(height):
        for j in range(weight):
            rotate_arr[weight-j-1][i] = arr[i][j]
    return rotate_arr

# 배열을 시계방향으로 90도 회전하는 함수
def rotate_clock(arr):
    height = len(arr)
    weight = len(arr[0])
    rotate_arr = [[0] * height for _ in range(weight)]
    for i in range(height):
        for j in range(weight):
            rotate_arr[j][height-i-1] = arr[i][j]
    return rotate_arr

# 들어온 배열을 반시계 방향으로 돌려 sort_r 함수 재사용
# 반환된 배열을 다시 시계 방향으로 돌려 원하는 값 으로 만듬
def sort_c(arr):
    arr_temp = rotate_rever_clock(arr)
    arr_temp = sort_r_use_heapq(arr_temp)
    arr_temp = rotate_clock(arr_temp)
    return arr_temp


for test_case in range(1,T+1):
    r,c,k = map(int,input().split())
    x_len, y_len = 3,3
    arr = [list(map(int,input().split())) for _ in range(x_len)]

    ans = -1
    for time in range(101):
        # r,c 가 초기 배열 사이즈를 벗어나는 경우 방지
        if r <= len(arr) and c <= len(arr[0]):
            if arr[r - 1][c - 1] == k:
                ans = time
                break
        if len(arr) >= len(arr[0]):
            arr = sort_r_use_heapq(arr)
        else:
            arr = sort_c(arr)
    print(ans)