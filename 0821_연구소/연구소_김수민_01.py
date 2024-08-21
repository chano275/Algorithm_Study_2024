import itertools
import copy

def make_two(copy):
    for i in range(row):
        try :
            index=copy[i].index(2)
            if i > 0 and copy[i-1][index] == 0 :
                    copy[i-1][index] = 2
            if i < row-1 and copy[i+1][index] == 0 :
                copy[i+1][index] = 2
            # if index > 0 and copy[i][index-1] == 0 :
            #     copy[i][index-1] = 2
            # if index < col-1 and copy[i][index+1] == 0 :
            #     copy[i][index+1] = 2
            if index > 0 :
                for j in range(index,-1,-1):
                    if copy[i][j] != 1 :
                        copy[i][j] = 2
                    else :
                        break
            if index < col -1 :
                for j in range(index,col):
                    if copy[i][j] != 1:
                        copy[i][j]=2
                    else :
                        break
        except ValueError :
            continue


def count_zero(copy):
    cnt=0
    for i in range(row):
        for j in range(col):
            if copy[i][j]==0 : cnt += 1
    return cnt

def built_wall(make_zero) :
    length=len(make_zero)
    max_wall=0
    for i in range(length) :
        copy_arr=copy.deepcopy(arr)
        for j in range(3):
            c_row,c_col=make_zero[i][j]
            copy_arr[c_row][c_col]=1
        make_two(copy_arr)
        comp=count_zero(copy_arr)
        max_wall=max(max_wall, comp)
    return max_wall

row, col=map(int,input().split())
arr=[list(map(int, input().split())) for _ in range(row)]
where_zero=[]

for i in range(row):
    for j in range(col):
        if arr[i][j]==0 :
            where_zero.append([i,j])

make_zero=list(itertools.combinations(where_zero,3))

print(built_wall(make_zero))