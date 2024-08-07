n = 0

# dfs와 같은 방식으로 풀기 위해 시도하다가 dfs로 못 구현하는 것보다 그냥 for문으로 구현하자해서 구현 진행해보게 됨


def can_build(heights, m):
    global n
    used = [False] * n

    for i in range(n - 1):
        if heights[i] == heights[i + 1]:            # 높이가 같은 경우 시간을 줄이기 위해 continue 진행
            continue

        # 높이 차이가 1인 경우에만 경사로 설치 가능
        elif abs(heights[i] - heights[i + 1]) == 1:
            if heights[i] < heights[i + 1]:         # 올라가는 경사로
                for j in range(m):                  # 경사로의 가로 길이 범위 안에서 비교를 진행하는데 경사로가 범위를 벗어나거나 이전의 위치에 경사로를 사용했거나 경사로를 설치할 곳이 일자가 아닌 경우
                    if i - j < 0 or used[i - j] or heights[i] != heights[i - j]:
                        return False
                    used[i - j] = True

            else:                                   # 내려가는 경사로
                for j in range(1, m + 1):
                    if i + j >= n or used[i + j] or heights[i + 1] != heights[i + j]:
                        return False
                    used[i + j] = True

        # for j를 도는 m의 값이 다른 이유는 올라가는 경사로를 검사할 때 i는 경사로가 설치되는 위치도 포함이지만
        # 내려가는 경사로를 검사할 때 i는 경사로를 설치하기 한 칸 전의 위치이기 때문에 1부터 시작해서 검사를 진행
        # ex) 33222 내려가는 경사 heights[1]일 때 elif문 들어옴 이 때 i의 위치값은 3  내려가는 경사는 계속 오른쪽으로 진행해보고
        #     22233일 때 heights[2]일 때 elif문 들어옴 이 때 i의 위치값은 2          올라가는 경사는 계속 왼쪽으로 진행해보는 느낌

        else:  # 높이 차이가 1 이상인 경우
            return False
    return True


def main():
    global n
    T = int(input())
    for test_case in range(1, T + 1):
        n, m = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(n)]

        count = 0

        for i in range(n):                              # for문 하나 안에서 가로 세로 다 처리할 수 있는 방법이 없을까 고민했을 때
            if can_build(arr[i], m):
                count += 1
            column = [arr[j][i] for j in range(n)]      # 다음과 같은 방식으로 진행가능 하다는 것을 gpt의 도움을 조금 받음...
                                                        # 이 과정에서 list comprehension이 정말 좋구나를 알게됨
            if can_build(column, m):
                count += 1

        print(f"#{test_case} {count}")


if __name__ == "__main__":
    main()
