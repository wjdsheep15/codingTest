"""
문제 설명
초밥이 색깔 접시로 제공되고, 색깔마다 가격이 달라요:

빨간 접시(R): $3

초록 접시(G): $4

파란 접시(B): $5

손님이 각 색깔 접시를 몇 개 골랐는지 알려줄 때, 총 가격을 계산해야 해요.

🔸 입력
첫 번째 줄: 빨간 접시 개수 R (0 이상 정수)

두 번째 줄: 초록 접시 개수 G (0 이상 정수)

세 번째 줄: 파란 접시 개수 B (0 이상 정수)

🔸 출력
식사의 총 가격 C를 출력 (단위: 달러)
"""
import sys
input = sys.stdin.readline

r = int(input())
g = int(input())
b = int(input())

print(3 * r + 4 * g + 5 * b)