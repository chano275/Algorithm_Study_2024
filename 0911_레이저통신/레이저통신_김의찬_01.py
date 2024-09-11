# https://www.acmicpc.net/problem/6087
import sys
sys.stdin = open('input_6087.txt','r')

import heapq

def BFS(xy):
    x,y = xy
    h_que = []
    distance[x][y]=0
    for d in range(4):
        heapq.heappush(h_que,(0,x,y,d))

    while h_que:
        cost,_x,_y,_d = heapq.heappop(h_que)
        distance[_x][_y] = cost
        if temp[_x][_y] == 'C': return cost
        for d in range(4):
            if (d+2) % 4 == _d: continue
            nx,ny = _x+dx[d],_y+dy[d]
            if 0 <= nx < H and 0 <= ny < W and temp[nx][ny] != '*' and distance[nx][ny] == -1 and (nx,ny) not in visited:
                if d == _d:
                    heapq.heappush(h_que,(cost,nx,ny,d))
                    visited.add((nx,ny))
                else: heapq.heappush(h_que,(cost+1,nx,ny,d))

W,H = map(int,input().split())
temp = [list(map(str,input().rstrip())) for _ in range(H)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
distance = [[-1]*W for _ in range(H)]
visited = set()
flag = False
for i in range(H):
    for j in range(W):
        if temp[i][j] == 'C':
            temp[i][j] = '*'
            ans = BFS((i,j))
            flag= True
            break
    if flag: break
print(ans)