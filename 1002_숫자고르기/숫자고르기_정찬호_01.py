# 브루트포스 < 수정 예정 

from itertools import combinations


n = int(input())
first = [i for i in range(1, n+1)]
next = [int(input()) for _ in range(n)]

# print(first, next)

first_set = set(first)
next_set = set(next)

if len(first_set) == len(next_set):
    print(n)
else:
    flag = 0
    for i in range(len(next_set), 0, -1):
        test = combinations(first, i)

        for chk in test:
            temp = set()

            for c in chk:
                if next[c-1] in temp:break
                temp.add(next[c-1])
            
            if temp == set(chk):
                # print(temp, chk)
                print(len(temp))
                temp_list = sorted(list(temp))
                for t in temp_list:print(t)
                flag = 1
            
            if flag == 1:break
        if flag == 1:break