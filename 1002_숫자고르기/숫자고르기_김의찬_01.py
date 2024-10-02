# https://www.acmicpc.net/problem/2668
import sys
sys.stdin = open('input_2668.txt','r')

def DFS(store_start,start,visited):
    global ans
    if store_start == start:
        ans.update(visited)
        return
    if start in visited:
        return
    visited.add(start)
    DFS(store_start,num[start],visited)


N = int(input())
num = [0] + [int(input()) for _ in range(N)]

ans = set()
visited = [False] * (N+1)
for now in range(1,N+1):
    temp_set = set()
    if visited[now]:
        continue
    temp_set.add(now)
    DFS(now,num[now],temp_set)
    visited[now] = True

print(len(ans))
list_ans = list(ans)
list_ans.sort()
for i in list_ans:
    print(i)