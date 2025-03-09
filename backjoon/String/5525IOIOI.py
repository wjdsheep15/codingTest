'''
N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.

P1 IOI
P2 IOIOI
P3 IOIOIOI
PN IOIOI...OI (O가 N개)
I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.

출력
S에 PN이 몇 군데 포함되어 있는지 출력한다.

1
13
OOIOIOIOIIOII

4
'''

# 50점 풀이
# import sys
# input = sys.stdin.readline
#
# p = 'OI'
# p1 = 'IOI'
#
# N = int(input())
# T = int(input())
# S = input().strip()
#
# pn = p1 + p * (N-1)
# cnt = 0
#
# for i in range(0, T - len(pn)+1):
#     temp = S[i: i + len(pn)]
#     if temp == pn:
#         cnt += 1
#     else:
#         continue
#
# print(cnt)


#100 점 풀이
import sys
input = sys.stdin.readline

N = int(input())  # PN의 N 값
T = int(input())  # 문자열 S의 길이
S = input().strip()  # 문자열 S

count = 0  # Pn 개수 카운트
i = 0  # 현재 탐색할 인덱스
pattern_length = 0  # 연속된 IOI 패턴 개수

while i < T - 1:
    if S[i:i+3] == "IOI":  # IOI 패턴 발견
        pattern_length += 1
        if pattern_length >= N:
            count += 1  # Pn 패턴이 완성되면 카운트 증가
        i += 2  # IOI는 2칸씩 증가하며 탐색
    else:
        pattern_length = 0  # 패턴이 끊기면 초기화
        i += 1  # 1칸 이동

print(count)