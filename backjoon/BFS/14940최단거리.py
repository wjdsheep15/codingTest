'''
문제
지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.

문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.

입력
지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)

다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.

출력
각 지점에서 목표지점까지의 거리를 출력한다. 원래 갈 수 없는 땅인 위치는 0을 출력하고, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.
'''
from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and result[nx][ny] == -1 and graph[nx][ny] != 0:
                result[nx][ny] = result[x][y] + 1
                queue.append((nx, ny))


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[-1] * m for _ in range(n)]  # 초기 거리를 -1로 설정

queue = deque()

# 목표 지점(2) 위치 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            queue.append((i, j))
            result[i][j] = 0  # 목표 지점은 거리 0
        elif graph[i][j] == 0:
            result[i][j] = 0  # 벽(0)은 그대로 유지

bfs()

# 결과 출력
for row in result:
    print(" ".join(map(str, row)))

