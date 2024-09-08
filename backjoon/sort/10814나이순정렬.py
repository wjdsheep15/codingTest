'''
3
21 Junkyu
21 Dohyun
20 Sunyoung
'''
# import sys
# input = sys.stdin.readline
# loop = int(input())
# age_list = []
# for _ in range(0, loop):
#     a, b = map(str, input().split())
#     if len(age_list) == 0:
#         age_list.append([a, b])
#     else:
#         for i in range(0, len(age_list)):
#             if int(a) >= int(age_list[i][0]) and i != len(age_list)-1:
#                 continue
#             elif int(a) < int(age_list[i][0]):
#                 age_list.insert(i, [a, b])
#                 break
#             else:
#                 age_list.append([a, b])
#                 break
#
# for i in range(0, len(age_list)):
#     print(age_list[i][0], age_list[i][1])
#
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


