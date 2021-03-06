
import sys
import copy

# 정점 개수.
n = int(input())

# 그래프, 복사 그래프 설정.
field = [[int(i) for i in input().split()] for j in range(n)]
field_copy = copy.deepcopy(field)

# 플로이드 와샬 알고리즘.
for k in range(n):
    for i in range(n):
        for j in range(n):
            # i k j 가 모 두같으면 비교 의미가 없음.
            if i == k or k == j: continue
            # i -> k + k -> j 가 i -> j 보다 작으면 시간의 합을 출력하지못함.
            if field[i][k] + field[k][j] < field[i][j]:
                print(-1)
                sys.exit()
            # i -> k + k -> J 와 i -> j 가 같으면 i -> j의 경우를 제외시킨다.
            elif field[i][k] + field[k][j] == field[i][j]:
                field_copy[i][j] = 0

# 제외시킬것들 제외한 복사된 곳에서 존재하는 값들을 모두 더함.
count = 0
for i in range(len(field_copy)):
    for j in range(len(field_copy)):
        count += field_copy[i][j]

# 대각선을 기준으로 대칭이기때문에 2로 나눈다.
print(count//2)
