T = int(input())
for test_case in range(1,T+1):
    N,M,K = map(int,input().split())
    now_shell = {}
    next_shell = {}

    for _ in range(K):
        x,y,n,d = map(int,input().split())
        if d == 1:
            now_shell[(x,y)] = (n,0,n)
        if d == 2:
            now_shell[(x,y)] = (n,2,n)
        if d == 3:
            now_shell[(x,y)] = (n,1,n)
        if d == 4:
            now_shell[(x,y)] = (n,3,n)

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    for _ in range(M):
        for virus in now_shell:
            x,y = virus
            n,d ,max_n = now_shell[virus]
            add_x = x + dx[d]
            add_y = y + dy[d]
            if add_x == 0 or add_x == N-1 or add_y == 0 or add_y == N-1:
                n = n//2
                d = (d+2)%4
            if n == 0:
                continue
            if (add_x,add_y) not in next_shell:
                next_shell[(add_x,add_y)] = (n,d,n)
            else:
                next_n , next_d, next_max_n = next_shell[(add_x,add_y)]
                if next_max_n < n :
                    next_shell[(add_x, add_y)] = (n + next_n, d, max_n)
                else:
                    next_shell[(add_x, add_y)] = (n + next_n, next_d, next_max_n)

        now_shell = next_shell.copy()
        next_shell.clear()

    ans = 0
    for i in now_shell:
        ans += now_shell[i][0]
    print(f'#{test_case} {ans}')