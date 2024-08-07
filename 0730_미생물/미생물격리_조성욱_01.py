T = int(input())

for test_case in range(1, T + 1):

	size, time, micro_set = list(map(int, input().split()))
	micro_list = [list(map(int, input().split())) for _ in range(micro_set)]

	move_dict = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

	for _ in range(time):
		temp_micro_dict = {}
		## 이동하고 micro dict에 정보 추가
		for micro in micro_list:
			dx, dy = move_dict[micro[3]]
			micro[0] += dx
			micro[1] += dy

			if micro[0] <= 0 or micro[0] >= 6 or micro[1] <= 0 or micro[1] >= 6:  # 약품에 닿으면
				micro[0] += -dx
				micro[1] += -dy
				micro[2] //= 2  # 미생물 절반
				if micro[3] == 1:  # 방향 전환
					micro[3] = 2
				elif micro[3] == 2:
					micro[3] = 1
				elif micro[3] == 3:
					micro[3] = 4
				else:
					micro[3] = 3

			if (micro[0], micro[1]) not in temp_micro_dict:  # 해당 좌표에 없으면 새로 넣음
				temp_micro_dict[(micro[0], micro[1])] = [(micro[2], micro[3])]
			else:  # 해당 좌표에 있으면 미생물 추가
				temp_micro_dict[(micro[0], micro[1])].append((micro[2], micro[3]))

		for micro_key, micro_value in temp_micro_dict.items():
			if len(micro_value) > 1:  ## 한 좌표에 두 개 이상의 미생물이 있으면 각각의 하나로 뭉치고 방향 지정
				new_direc, new_num = 0, 0
				for direction, micro_num in micro_value:
					new_num += micro_num  ## 같은 좌표 미생물 더함
					if micro_num > new_num:
						new_direc = direction  ## 가장 큰 미생물의 방향

				x, y = micro_key
				micro_list.append([x, y, new_direc, new_num])  ## 새로 생긴 미생물 저장

			else:  ## 한 좌표에 하나의 미생물만 있는 경우
				micro_list.append(list(micro_key) + list(micro_value))
	res = 0
	for x, y, direction, micro_num in micro_list:
		res += micro_num

	print(micro_num)


	for a in b:
		a는 복사해온 것.
		a를 컨트롤해도 b는 바꾸지 못함