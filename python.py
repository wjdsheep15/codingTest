# a1 = [[0] * 5] * 3
# a1[1][1] = 99
# print(a1)
#
#
# a2 = [[0] * 5 for _ in range(3)]
# a2[1][1] = 99
# print(a2)


import sys
import time

# 테스트 입력 데이터: 100,000개의 숫자 입력
n = 3

# 1. input() 함수로 입력 처리
start_time = time.time()
for _ in range(n):
    data = input()  # 이 부분에서 사용자 입력이 필요함
end_time = time.time()
print(f"input() 사용 시간: {end_time - start_time}초")

# 2. sys.stdin.readline으로 입력 처리
start_time = time.time()
for _ in range(n):
    data = sys.stdin.readline().strip()
end_time = time.time()
print(f"sys.stdin.readline() 사용 시간: {end_time - start_time}초")