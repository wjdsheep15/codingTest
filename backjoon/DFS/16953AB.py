"""
문제
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다.
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

입력
첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

출력
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

예제 입력 1
2 162
예제 출력 1
5
2 → 4 → 8 → 81 → 162
"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(A, B):
    queue = deque([(A, 1)])

    while queue:
        num, cnt = queue.popleft()
        if num == B:
            return cnt  # 목표 도달 시 횟수 반환

        if num * 2 <= B:
            queue.append((num * 2, cnt + 1))

        if num * 10 + 1 <= B:
            queue.append((num * 10 + 1, cnt + 1))

    return -1  # 도달 불가능한 경우


A, B = map(int, input().split())
print(bfs(A, B))
