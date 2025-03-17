'''
한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.



N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.

다음 예는 22 × 22 크기의 배열을 방문한 순서이다.



N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

다음은 N=3일 때의 예이다.



입력
첫째 줄에 정수 N, r, c가 주어진다.

출력
r행 c열을 몇 번째로 방문했는지 출력한다.

제한
1 ≤ N ≤ 15
0 ≤ r, c < 2N

예제 입력 1
2 3 1
예제 출력 1
11
예제 입력 2
3 7 7
예제 출력 2
63
'''

import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

result = 0
size = 2 ** N
while size > 1:
    size //= 2  # 4등분을 위한 절반 크기

    # 사분면 판별
    if r < size and c < size:  # 1사분면 (왼쪽 위)
        pass  # 기존 result 유지
    elif r < size and c >= size:  # 2사분면 (오른쪽 위)
        result += size * size  # 1/4 만큼 더하기
        c -= size
    elif r >= size and c < size:  # 3사분면 (왼쪽 아래)
        result += 2 * size * size  # 2/4 만큼 더하기
        r -= size
    else:  # 4사분면 (오른쪽 아래)
        result += 3 * size * size  # 3/4 만큼 더하기
        r -= size
        c -= size

print(result)