from collections import Counter

def check_rotate(li_c):
    row_len=len(li_c)
    col_len=len(li_c[0])
    li_rl=[[0 for _ in range(row_len)]for _ in range(col_len)]
    for i in range(row_len):
        for j in range(col_len):
            li_rl[j][row_len-1-i]=li_c[i][j]

    return li_rl, True

def back_rotate(li_b):
    row_len=len(li_b)
    col_len=len(li_b[0])
    li_rb=[[0 for _ in range(row_len)]for _ in range(col_len)]
    
    for i in range(row_len):
        for j in range(col_len):
            li_rb[j][i]=li_b[i][j]

    return li_rb

def sort_array(arr,rotate_status):
    row_len=len(arr)
    col_len=len(arr[0])

    if col_len>row_len:
        li_ro, rotate_status=check_rotate(arr)
        arr=[k[:] for k in li_ro]
    
    row_len=len(arr)
    col_len=len(arr[0])
    
    li_rs=[[] for _ in range(row_len)]

    for i in range(row_len):
        li_fi=[k for k in arr[i] if k != 0]
        freq = Counter(li_fi)
        li_rt = [[alpha, beta] for alpha, beta in freq.items()]
        li_rt_so = sorted(li_rt, key=lambda x: (x[1], x[0]))
        li_rs[i]=[alpha for beta in li_rt_so for alpha in beta]

    max_rows=min(len(li_rs), 100)
    max_cols=min(max(len(row_lo) for row_lo in li_rs),100)
    li_rs_ap = [row_lo[:max_cols] + [0] * (max_cols - len(row_lo)) for row_lo in li_rs[:max_rows]]
 
    if rotate_status:
        li_rs_ap = back_rotate(li_rs_ap)
        rotate_status = False       

    return li_rs_ap, rotate_status

row,col,num = map(int,input().split())
row -= 1
col -= 1
arr=[list(map(int, input().split())) for _ in range(3)]
result=0
rotate_status=False
if len(arr) > row and len(arr[0]) >col and arr[row][col] == num :
    print (0)
else :
    while result <= 100 :
        arr, rotate_status=sort_array(arr, rotate_status)
        result += 1
        if len(arr) > row and len(arr[0]) >col and arr[row][col] == num :
            print(result)
            break

if result > 100 :
    print(-1)