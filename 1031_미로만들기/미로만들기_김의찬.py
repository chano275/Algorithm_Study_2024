# https://www.acmicpc.net/problem/2665
import sys
sys.stdin = open('input_2665.txt','r')

import heapq

def BFS():
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    h_que = []
    cnt = [[float('inf')]*N for _ in range(N)]
    cnt[0][0] = 0
    heapq.heappush(h_que,(0,(0,0)))
    while h_que:
        black,(x,y) = heapq.heappop(h_que)
        if (x,y) == (N-1,N-1):
            return black
        if cnt[x][y] < black: continue
        for d in range(4):
            nx,ny = x+dx[d], y+dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if maze[nx][ny] == 0:
                    black_temp = black+1
                else:
                    black_temp = black

                if black_temp < cnt[nx][ny]:
                    cnt[nx][ny] = black_temp
                    heapq.heappush(h_que,(black_temp,(nx,ny)))



N = int(input())
maze = [list(map(int,input().rstrip())) for _ in range(N)]

ans = BFS()
print(ans)