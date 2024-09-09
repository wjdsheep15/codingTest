'''
3
21 Junkyu
21 Dohyun
20 Sunyoung
'''
import sys

input = sys.stdin.readline

# 입력 받을 사람 수
loop = int(input())
age_list = []

# 입력 처리
for _ in range(loop):
    a, b = map(str, input().split())
    age_list.append((int(a), b))  # 나이를 정수형으로 변환하여 튜플로 저장

# 나이 기준으로 정렬
age_list.sort(key=lambda x: x[0])

# 결과 출력
for age, name in age_list:
    print(age, name)


