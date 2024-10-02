def dfs(_start, cur, _visited):
    start_visited[cur] = True

    _next = second[cur]

    if _next == _start:  # 시작한 지점으로 돌아오는 사이클 발견
        cycle_length = len(_visited)
        _visited = sorted(_visited)
        if cycle_length in ans_dict:
            if _visited not in ans_dict[cycle_length]:
                ans_dict[cycle_length].append(_visited)
        else:
            ans_dict[cycle_length] = [_visited]
        return

    elif _next in _visited:  # 중간에 사이클 발견
        start_visited[_next] = True
        target = _visited[_visited.index(_next):]
        cycle_length = len(target)
        target = sorted(target)
        if cycle_length in ans_dict:
            if target not in ans_dict[cycle_length]:
                ans_dict[cycle_length].append(target)
        else:
            ans_dict[cycle_length] = [target]
        return

    if start_visited[_next]:
        return

    _visited.append(_next)
    dfs(_start, _next, _visited)
    _visited.pop()

    return

n = int(input())
first = [-1] + [i for i in range(1, n + 1)]
second = [-1] + [int(input()) for _ in range(n)]
start_visited = [False] * (n+1)
ans_dict = {}

for i in range(1, n+1):
    if start_visited[i]:
        continue
    dfs(i, i, [i])

# 모든 사이클의 숫자를 결과에 포함
temp = set()
for cycle_length in ans_dict:
    for v in ans_dict[cycle_length]:
        temp.update(v)
print(len(temp))
for t in sorted(temp):
    print(t)
