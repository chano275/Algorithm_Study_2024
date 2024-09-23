# https://www.acmicpc.net/problem/4991
import sys
sys.stdin = open('input_4991.txt','r')

from itertools import permutations
from collections import deque

def copy_arr(arr):
    temp = [i[:] for i in arr]
    return temp

def BFS(start,end):
    if (start,end) in dist_memo:
        return dist_memo[(start,end)]

    d_que = deque()
    d_que.append((start,0))
    copy_room = copy_arr(room)
    copy_room[start[0]][start[1]] = 'x'
    while d_que:
        now,dist = d_que.popleft()
        if now == end:
            dist_memo[(start,end)] = dist
            dist_memo[(end,start)] = dist
            return dist
        for d in range(4):
            nx, ny = now[0] + dx[d] , now[1] + dy[d]
            if 0 <= nx < M and 0 <= ny < N and copy_room[nx][ny] != 'x':
                copy_room[nx][ny] = 'x'
                d_que.append(((nx,ny),dist+1))
    return -1

while True:
    N,M = map(int,input().split())
    if N == 0 and M == 0:
        break
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    dist_memo = {}
    room = [list(map(str,input())) for _ in range(M)]
    dust = []
    for i in range(M):
        for j in range(N):
            if room[i][j] == 'o':
                robot = (i,j)
            elif room[i][j] == '*':
                dust.append((i,j))
    flag = True
    for check_dust in dust:
        check_zero = BFS(robot,check_dust)
        if check_zero == -1:
            print(-1)
            flag = False
            break
    if flag:
        ans = float('inf')
        for per in permutations(dust,len(dust)):
            now_robot = robot
            temp_ans = 0
            for next in per:
                temp = BFS(now_robot,next)
                temp_ans += temp
                if temp_ans > ans:break
                now_robot = next
            ans = min(ans,temp_ans)
        print(ans)
