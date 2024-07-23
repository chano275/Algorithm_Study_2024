import sys

from collections import deque

sys.stdin = open('input_2477.txt','r')

T = int(input())
# T = 4
for test_case in range(1,T+1):
    # 접수창구 갯수, 정비창구 갯수, 사람수, 목표 접수창구, 목표 정비창구
    N,M,K,A,B = map(int,input().split())
    # 접수창구별 걸리는 시간
    a_time = list(map(int,input().split()))
    # 정비창구별 걸리는 시간
    b_time = list(map(int,input().split()))
    # 사람이 입장하는 시간
    p_time = list(map(int,input().split()))

    # 시간 흐름을 측정하기 위한 변수
    real_time = 0
    # 끝난 사람을 체크할 리스트
    end_people = []
    # 입장시간이 경과하여 빈 접수창구 기다리는 deque
    wait_person = deque()
    # 접수창구에서 작업중
    receptioning = [(0,-1) for _ in range(N)]
    # 접수창구에서 나와 빈 정비창구를 기다리는 deque
    wait_repair = deque()
    # 정비창구에서 작업중
    repairing = [(0,-1) for _ in range(M)]
    # 큐에 중복으로 들어가지 않기 위함
    check_people =[True for _ in range(K)]
    # 목표 접수창구에 방문한 사람을 저장
    check_recption=[]
    # 목표 정비창구에 방문한 사람을 저장
    check_repair = []

    flag = True
    # 모든 사람이 끝날때 까지 반복
    while len(end_people) < K:
        flag = True
        # 사람별 입장시간을 확인하여 해당하는 사람을 접수처 대기 큐에 추가
        for i,p in enumerate(p_time):
            if check_people[i] and p == real_time :
                wait_person.append(i+1)
                # 혹시 모를 중복을 대비한 false
                check_people[i] = False
        # 접수창구에 작업중인 사람이 있다면 끝났는지 확인 하여 끝났다면 정비창구 대기줄에 추가
        # 대기줄에 추가는 사람의 인덱스
        for idx1, (person_idx1, check_time1) in enumerate(receptioning):
            if check_time1 == real_time:
                receptioning[idx1] = (0, -1)
                wait_repair.append(person_idx1)

        # 접수창구를 기다리는 사람이 있을때 빈 접수창구가 있다면 접수창구에 입장함
        # 접수창구에 입장할때 튜플로 (사람의 인덱스 번호와 필요한 시간)을 저장
        # 만약 목표 접수창구라면 사람의 인덱스 저장하기
        # 접수창구를 기다리는 사람이 존재하지만 빈 접수창구가 없다면 break
        while wait_person:
            if (0,-1) in receptioning:
                person_idx = wait_person.popleft()
                empty_reception = receptioning.index((0,-1))
                receptioning[empty_reception] = (person_idx,real_time + a_time[empty_reception])
                if empty_reception == A-1:
                    check_recption.append(person_idx)
            else:
                break
        # 접수창구에 작업중인 사람이 있다면 끝났는지 확인하여 끝났다면
        # 접수창구를 초기화 하고 정비창구 대기줄에 추가
        for idx1, (person_idx1,check_time1) in enumerate(receptioning):
            if check_time1 == real_time:
                receptioning[idx1] = (0,-1)
                wait_repair.append(person_idx1)
                flag = False

        # 정비창구에 작업중인 사람이 있다면 끝났는지 확인하여 끝났다면
        # 정비창구를 초기화하고 끝난사람들 리스트에 저장
        for idx2, (person_idx2,check_time2) in enumerate(repairing):
            if check_time2 == real_time:
                repairing[idx2] =(0,-1)
                end_people.append(person_idx2)

        # 정비창구를 기다리는 사람이 있을때 빈 정비창구가 있다면 정비창구에 입장함
        # 정비창구에 입장할때 튜플로 (사람의 인덱스 번호와 필요한 시간)을 저장
        # 만약 목표 정비창구라면 사람의 인덱스 저장하기
        # 접수창구를 기다리는 사람이 존재하지만 빈 접수창구가 없다면 break
        while wait_repair:
            if (0,-1) in repairing:
                person_idx = wait_repair.popleft()
                empty_repair = repairing.index((0,-1))
                repairing[empty_repair] = (person_idx,real_time + b_time[empty_repair])
                if empty_repair == B-1:
                    check_repair.append(person_idx)
                flag = False
            else:
                break
        # 정비창구에 작업중인 사람이 있다면 끝났는지 확인하여 끝났다면
        # 정비창구를 초기화하고 끝난사람들 리스트에 저장
        for idx2, (person_idx2,check_time2) in enumerate(repairing):
            if check_time2 == real_time:
                repairing[idx2] =(0,-1)
                end_people.append(person_idx2)

                flag = False

        if flag: real_time += 1
    ans = 0

    for i in check_recption:
        if i in check_repair:
            ans += i

    if ans != 0:
        print(f'#{test_case} {ans}')
    else:
        print(f'#{test_case} -1')

